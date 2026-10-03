from backend.services.assessment_engine import assess_answers, validate_answers

def simulate_improvement(answers, changes):
    errors = validate_answers(answers)
    if errors:
        raise ValueError("; ".join(errors))
    current = assess_answers(answers)
    improved_answers = dict(answers)
    for key, value in changes.items():
        if key in improved_answers:
            improved_answers[key] = value
    simulated = assess_answers(improved_answers)
    return {
        "educational_simulation": True,
        "current_score": current["overall_score"],
        "current_level": current["risk_level"],
        "simulated_score": simulated["overall_score"],
        "simulated_level": simulated["risk_level"],
        "risk_reduction": round(current["overall_score"] - simulated["overall_score"], 2),
        "simulated_category_scores": simulated["category_scores"],
        "changed_fields": list(changes.keys()),
        "disclaimer": "Simulation only; it is not a guarantee of real-world safety or compromise prevention."
    }
