import json
import sqlite3
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS assessments (
    assessment_id TEXT PRIMARY KEY,
    overall_score REAL NOT NULL,
    risk_level TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS category_scores (
    category_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id TEXT NOT NULL,
    category TEXT NOT NULL,
    score REAL NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);
CREATE TABLE IF NOT EXISTS findings (
    finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id TEXT NOT NULL,
    category TEXT NOT NULL,
    finding_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);
CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assessment_id TEXT NOT NULL,
    finding_type TEXT NOT NULL,
    recommendation TEXT NOT NULL,
    priority TEXT NOT NULL,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);
"""

def connect(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(path):
    conn = connect(path)
    conn.executescript(SCHEMA)
    conn.close()

def save_assessment(path, result):
    conn = connect(path)
    try:
        conn.execute(
            "INSERT INTO assessments VALUES (?, ?, ?, ?)",
            (result["assessment_id"], result["overall_score"], result["risk_level"], result["created_at"])
        )
        for category, score in result["category_scores"].items():
            conn.execute(
                "INSERT INTO category_scores (assessment_id, category, score) VALUES (?, ?, ?)",
                (result["assessment_id"], category, score)
            )
        for f in result["findings"]:
            conn.execute(
                """INSERT INTO findings
                (assessment_id, category, finding_type, severity, description)
                VALUES (?, ?, ?, ?, ?)""",
                (result["assessment_id"], f["category"], f["finding_type"], f["severity"], f["description"])
            )
        for r in result["recommendations"]:
            conn.execute(
                """INSERT INTO recommendations
                (assessment_id, finding_type, recommendation, priority)
                VALUES (?, ?, ?, ?)""",
                (result["assessment_id"], r["finding_type"], r["recommendation"], r["priority"])
            )
        conn.commit()
    finally:
        conn.close()

def get_assessment(path, assessment_id):
    conn = connect(path)
    try:
        row = conn.execute("SELECT * FROM assessments WHERE assessment_id=?", (assessment_id,)).fetchone()
        if not row:
            return None
        categories = {
            r["category"]: r["score"]
            for r in conn.execute(
                "SELECT category, score FROM category_scores WHERE assessment_id=?",
                (assessment_id,)
            ).fetchall()
        }
        findings = [dict(r) for r in conn.execute(
            "SELECT category, finding_type, severity, description FROM findings WHERE assessment_id=? ORDER BY finding_id",
            (assessment_id,)
        ).fetchall()]
        recommendations = [dict(r) for r in conn.execute(
            "SELECT finding_type, recommendation, priority FROM recommendations WHERE assessment_id=? ORDER BY recommendation_id",
            (assessment_id,)
        ).fetchall()]
        return {
            "assessment_id": row["assessment_id"],
            "overall_score": row["overall_score"],
            "risk_level": row["risk_level"],
            "created_at": row["created_at"],
            "category_scores": categories,
            "findings": findings,
            "recommendations": recommendations,
            "privacy_note": "Raw questionnaire answers and sensitive personal values are not stored."
        }
    finally:
        conn.close()

def get_dashboard_stats(path):
    conn = connect(path)
    try:
        total = conn.execute("SELECT COUNT(*) AS n FROM assessments").fetchone()["n"]
        distribution = {
            level: conn.execute(
                "SELECT COUNT(*) AS n FROM assessments WHERE risk_level=?", (level,)
            ).fetchone()["n"]
            for level in ["LOW","MODERATE","HIGH","CRITICAL"]
        }
        avg = conn.execute("SELECT AVG(overall_score) AS avg FROM assessments").fetchone()["avg"]
        cat = conn.execute(
            "SELECT category, AVG(score) AS avg_score FROM category_scores GROUP BY category ORDER BY avg_score DESC"
        ).fetchall()
        return {
            "total_assessments": total,
            "risk_distribution": distribution,
            "average_score": round(avg or 0, 2),
            "average_category_scores": [{"category": r["category"], "score": round(r["avg_score"],2)} for r in cat]
        }
    finally:
        conn.close()
