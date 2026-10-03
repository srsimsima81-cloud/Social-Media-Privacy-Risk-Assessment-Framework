import os
from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from backend.models.database import init_db, save_assessment, get_assessment, get_dashboard_stats
from backend.services.assessment_engine import validate_answers, assess_answers
from backend.services.improvement_simulator import simulate_improvement
from backend.services.report_generator import generate_html_report
from backend.services.checklist import PRIVACY_CHECKLIST

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

def create_app(testing=False):
    app = Flask(__name__, static_folder=None)
    app.config["TESTING"] = testing
    app.config["DATABASE_PATH"] = os.getenv(
        "DATABASE_PATH",
        os.path.join(BASE_DIR, "privacy_risk.db")
    )
    CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})

    init_db(app.config["DATABASE_PATH"])

    @app.get("/")
    def index():
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.get("/assessment")
    def assessment_page():
        return send_from_directory(FRONTEND_DIR, "assessment.html")

    @app.get("/dashboard")
    def dashboard_page():
        return send_from_directory(FRONTEND_DIR, "dashboard.html")

    @app.get("/simulator")
    def simulator_page():
        return send_from_directory(FRONTEND_DIR, "simulator.html")

    @app.get("/report/<assessment_id>")
    def report_page(assessment_id):
        record = get_assessment(app.config["DATABASE_PATH"], assessment_id)
        if not record:
            return "Assessment not found", 404
        return generate_html_report(record)

    @app.get("/css/<path:filename>")
    def css(filename):
        return send_from_directory(os.path.join(FRONTEND_DIR, "css"), filename)

    @app.get("/js/<path:filename>")
    def js(filename):
        return send_from_directory(os.path.join(FRONTEND_DIR, "js"), filename)

    @app.post("/api/assessment")
    def create_assessment():
        payload = request.get_json(silent=True) or {}
        answers = payload.get("answers", payload)

        errors = validate_answers(answers)
        if errors:
            return jsonify({"error": "Validation failed", "details": errors}), 400

        result = assess_answers(answers)
        save_assessment(app.config["DATABASE_PATH"], result)
        return jsonify(result), 201

    @app.get("/api/assessment/<assessment_id>")
    def read_assessment(assessment_id):
        record = get_assessment(app.config["DATABASE_PATH"], assessment_id)
        if not record:
            return jsonify({"error": "Assessment not found"}), 404
        return jsonify(record)

    @app.get("/api/assessment/<assessment_id>/recommendations")
    def recommendations(assessment_id):
        record = get_assessment(app.config["DATABASE_PATH"], assessment_id)
        if not record:
            return jsonify({"error": "Assessment not found"}), 404
        return jsonify({
            "assessment_id": assessment_id,
            "recommendations": record["recommendations"]
        })

    @app.post("/api/assessment/simulate-improvement")
    def improvement():
        payload = request.get_json(silent=True) or {}
        answers = payload.get("answers", {})
        changes = payload.get("changes", {})
        errors = validate_answers(answers)
        if errors:
            return jsonify({"error": "Validation failed", "details": errors}), 400
        return jsonify(simulate_improvement(answers, changes))

    @app.get("/api/dashboard/stats")
    def dashboard_stats():
        return jsonify(get_dashboard_stats(app.config["DATABASE_PATH"]))

    @app.get("/api/privacy-checklist")
    def checklist():
        return jsonify({"checklist": PRIVACY_CHECKLIST})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=True)
