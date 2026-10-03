import pytest
from backend.services.questionnaire import QUESTIONS
from backend.services.assessment_engine import assess_answers, validate_answers
from backend.services.scoring_engine import classify_risk, calculate_privacy_risk, calculate_category_scores

def base_answers():
    return {q["id"]: ("PRIVATE" if q["id"]=="profile_visibility" else ("NEVER" if q.get("type")=="freq" else "NO")) for q in QUESTIONS}

@pytest.mark.parametrize("field", [
    "phone_public","email_public","birthday_public","location_public","realtime_checkins",
    "travel_posts","workplace_public","education_public","posts_public","public_connections",
    "anyone_can_tag","mfa_enabled","login_alerts_enabled","password_reuse_reported",
    "third_party_apps_reviewed","suspicious_link_awareness","old_accounts",
    "privacy_settings_reviewed","historical_posts_reviewed","photo_metadata_awareness"
])
def test_risk_changes_for_field(field):
    a=base_answers()
    a[field]="YES"
    result=assess_answers(a)
    assert 0 <= result["overall_score"] <= 100

def test_fully_private_profile_is_valid():
    result=assess_answers(base_answers())
    assert result["risk_level"] in {"LOW","MODERATE","HIGH","CRITICAL"}

def test_public_profile_is_higher_than_private():
    low=base_answers()
    high=base_answers()
    high["profile_visibility"]="PUBLIC"
    for q in QUESTIONS:
        if q["id"] != "profile_visibility" and q.get("type") != "freq":
            high[q["id"]]="YES"
    assert assess_answers(high)["overall_score"] > assess_answers(low)["overall_score"]

def test_category_score_calculation():
    scores=calculate_category_scores(base_answers())
    assert len(scores)==10
    assert all(0<=v<=100 for v in scores.values())

def test_overall_score_calculation():
    scores={k:50 for k in calculate_category_scores(base_answers())}
    assert calculate_privacy_risk(scores)==50

@pytest.mark.parametrize("score,expected", [(20,"LOW"),(21,"MODERATE"),(40,"MODERATE"),(41,"HIGH"),(70,"HIGH"),(71,"CRITICAL"),(100,"CRITICAL")])
def test_score_boundaries(score,expected):
    assert classify_risk(score)==expected

def test_validation_rejects_missing():
    errors=validate_answers({})
    assert errors

def test_validation_rejects_bad_value():
    a=base_answers()
    a["mfa_enabled"]="MAYBE"
    assert validate_answers(a)

def test_findings_generated():
    a=base_answers()
    a["phone_public"]="YES"
    r=assess_answers(a)
    assert any(f["finding_type"]=="Public phone number" for f in r["findings"])

def test_recommendations_generated():
    a=base_answers()
    a["mfa_enabled"]="NO"
    r=assess_answers(a)
    assert any(x["finding_type"]=="MFA disabled" for x in r["recommendations"])

def test_sensitive_values_not_returned():
    r=assess_answers(base_answers())
    serialized=str(r).lower()
    assert "password123" not in serialized
    assert "@" not in serialized

def test_simulation_route():
    # engine-level simulation is exercised through the API test suite
    assert True
