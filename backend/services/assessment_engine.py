from uuid import uuid4
from datetime import datetime, timezone
from backend.services.questionnaire import QUESTIONS, ALLOWED_YN, ALLOWED_FREQ, ALLOWED_VIS
from backend.services.scoring_engine import extract_privacy_features, calculate_category_scores, calculate_privacy_risk, classify_risk
from backend.services.findings_engine import generate_privacy_findings
from backend.services.recommendation_engine import generate_recommendations

def validate_answers(answers):
    errors = []
    if not isinstance(answers, dict):
        return ["answers must be an object"]
    for q in QUESTIONS:
        qid = q["id"]
        if qid not in answers:
            errors.append(f"Missing answer: {qid}")
            continue
        val = str(answers[qid]).upper()
        allowed = ALLOWED_VIS if qid == "profile_visibility" else (
            ALLOWED_FREQ if q.get("type") == "freq" else ALLOWED_YN
        )
        if val not in allowed:
            errors.append(f"Invalid answer for {qid}: {val}")
    return errors

def assess_answers(answers):
    normalized = {k: str(v).upper() for k, v in answers.items()}
    features = extract_privacy_features(normalized)
    category_scores = calculate_category_scores(normalized, features)
    overall = calculate_privacy_risk(category_scores)
    level = classify_risk(overall)
    findings = generate_privacy_findings(normalized)
    recommendations = generate_recommendations(findings)
    return {
        "assessment_id": str(uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "overall_score": overall,
        "risk_level": level,
        "category_scores": category_scores,
        "findings": findings,
        "recommendations": recommendations,
        # Answers are deliberately NOT returned or stored.
        "privacy_note": "Only derived risk results are retained; sensitive personal values are not collected."
    }
