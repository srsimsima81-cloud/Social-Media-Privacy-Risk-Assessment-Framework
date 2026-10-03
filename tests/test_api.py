from backend.services.questionnaire import QUESTIONS

def valid_answers():
    return {q["id"]: ("PRIVATE" if q["id"]=="profile_visibility" else ("NEVER" if q.get("type")=="freq" else "NO")) for q in QUESTIONS}

def test_post_assessment(client):
    r=client.post("/api/assessment", json={"answers":valid_answers()})
    assert r.status_code==201
    assert r.json["assessment_id"]

def test_get_assessment(client):
    r=client.post("/api/assessment", json={"answers":valid_answers()})
    aid=r.json["assessment_id"]
    g=client.get(f"/api/assessment/{aid}")
    assert g.status_code==200
    assert "overall_score" in g.json

def test_get_recommendations(client):
    r=client.post("/api/assessment", json={"answers":valid_answers()})
    aid=r.json["assessment_id"]
    g=client.get(f"/api/assessment/{aid}/recommendations")
    assert g.status_code==200
    assert "recommendations" in g.json

def test_missing_assessment(client):
    assert client.get("/api/assessment/no-such-id").status_code==404

def test_dashboard_stats(client):
    r=client.get("/api/dashboard/stats")
    assert r.status_code==200
    assert "risk_distribution" in r.json

def test_checklist(client):
    r=client.get("/api/privacy-checklist")
    assert r.status_code==200
    assert len(r.json["checklist"]) >= 15

def test_simulation(client):
    answers=valid_answers()
    changes={"mfa_enabled":"YES","profile_visibility":"PRIVATE"}
    r=client.post("/api/assessment/simulate-improvement", json={"answers":answers,"changes":changes})
    assert r.status_code==200
    assert r.json["educational_simulation"] is True
    assert "simulated_score" in r.json

def test_bad_payload(client):
    r=client.post("/api/assessment", json={"answers":{}})
    assert r.status_code==400

def test_report_route(client):
    r=client.post("/api/assessment", json={"answers":valid_answers()})
    aid=r.json["assessment_id"]
    g=client.get(f"/report/{aid}")
    assert g.status_code==200
    assert b"Privacy Risk Assessment" in g.data

def test_frontend_pages(client):
    assert client.get("/").status_code==200
    assert client.get("/assessment").status_code==200
    assert client.get("/dashboard").status_code==200
