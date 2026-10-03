from backend.services.questionnaire import QUESTIONS, CATEGORIES

DEFAULT_WEIGHTS = {
    "Profile Visibility": 10,
    "Personal Information": 15,
    "Location Privacy": 15,
    "Posts & Content": 10,
    "Friends / Followers": 10,
    "Tagging & Mentions": 5,
    "Account Security": 15,
    "Third-Party Apps": 5,
    "Social Engineering": 10,
    "Digital Footprint": 5,
}

def response_risk(answer, reverse=False):
    """Convert an answer to 0-100 contribution. Higher means higher assessed risk."""
    if answer is None:
        return 50.0
    a = str(answer).upper()
    if a in {"PUBLIC"}:
        return 90.0
    if a in {"FRIENDS"}:
        return 35.0
    if a in {"PRIVATE"}:
        return 5.0

    if a in {"YES"}:
        return 10.0 if reverse else 85.0
    if a == "NO":
        return 85.0 if reverse else 10.0
    if a == "SOMETIMES":
        return 50.0
    if a == "NOT SURE":
        return 60.0

    if a == "NEVER":
        return 5.0 if not reverse else 85.0
    if a == "RARELY":
        return 25.0 if not reverse else 65.0
    if a == "OFTEN":
        return 80.0 if not reverse else 20.0
    if a == "ALWAYS":
        return 95.0 if not reverse else 5.0
    return 50.0

def extract_privacy_features(answers):
    features = {}
    for q in QUESTIONS:
        features[q["id"]] = response_risk(
            answers.get(q["id"]), q.get("reverse", False)
        )
    return features

def calculate_category_scores(answers, features=None):
    features = features or extract_privacy_features(answers)
    scores = {}
    for category in CATEGORIES:
        qs = [q for q in QUESTIONS if q["category"] == category]
        vals = [features[q["id"]] for q in qs]
        scores[category] = round(sum(vals) / len(vals), 2) if vals else 0.0
    return scores

def calculate_privacy_risk(category_scores, weights=None):
    weights = weights or DEFAULT_WEIGHTS
    total_weight = sum(weights.values())
    score = sum(category_scores[c] * weights[c] for c in weights) / total_weight
    score = round(max(0.0, min(100.0, score)), 2)
    return score

def classify_risk(score):
    if score <= 20:
        return "LOW"
    if score <= 40:
        return "MODERATE"
    if score <= 70:
        return "HIGH"
    return "CRITICAL"
