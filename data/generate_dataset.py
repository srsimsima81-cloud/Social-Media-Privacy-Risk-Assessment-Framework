import csv
import random
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from backend.services.questionnaire import QUESTIONS
from backend.services.assessment_engine import assess_answers

random.seed(42)

FIELDS = [
    "profile_id","profile_visibility","phone_public","email_public","birthday_public",
    "location_public","workplace_public","education_public","relationship_public",
    "posts_public","location_tagging","travel_posts","unknown_connections",
    "tag_review_enabled","third_party_apps_reviewed","mfa_enabled","login_alerts_enabled",
    "password_reuse_reported","suspicious_link_awareness","old_posts_reviewed",
    "privacy_settings_reviewed","risk_score","risk_level"
]

def make_answer(q):
    if q["id"] == "profile_visibility":
        return random.choices(["PUBLIC","FRIENDS","PRIVATE"], [0.35,0.45,0.20])[0]
    if q.get("type") == "freq":
        return random.choices(["NEVER","RARELY","SOMETIMES","OFTEN","ALWAYS"], [0.25,0.25,0.25,0.18,0.07])[0]
    return random.choices(["YES","NO","SOMETIMES","NOT SURE"], [0.18,0.57,0.15,0.10])[0]

def main(n=1000):
    out = ROOT / "data" / "social_media_privacy_assessments.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for i in range(1, n+1):
            answers = {q["id"]: make_answer(q) for q in QUESTIONS}
            result = assess_answers(answers)
            row = {
                "profile_id": f"SYN-{i:05d}",
                "profile_visibility": answers["profile_visibility"],
                "phone_public": answers["phone_public"],
                "email_public": answers["email_public"],
                "birthday_public": answers["birthday_public"],
                "location_public": answers["location_public"],
                "workplace_public": answers["workplace_public"],
                "education_public": answers["education_public"],
                "relationship_public": answers["relationship_public"],
                "posts_public": answers["posts_public"],
                "location_tagging": answers["geotagging"],
                "travel_posts": answers["travel_posts"],
                "unknown_connections": answers["unknown_connections"],
                "tag_review_enabled": answers["tag_review_enabled"],
                "third_party_apps_reviewed": answers["third_party_apps_reviewed"],
                "mfa_enabled": answers["mfa_enabled"],
                "login_alerts_enabled": answers["login_alerts_enabled"],
                "password_reuse_reported": answers["password_reuse_reported"],
                "suspicious_link_awareness": answers["suspicious_link_awareness"],
                "old_posts_reviewed": answers["historical_posts_reviewed"],
                "privacy_settings_reviewed": answers["privacy_settings_reviewed"],
                "risk_score": result["overall_score"],
                "risk_level": result["risk_level"],
            }
            writer.writerow(row)
    print(f"Generated {n} synthetic records: {out}")

if __name__ == "__main__":
    main()
