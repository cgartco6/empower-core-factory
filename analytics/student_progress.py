def predict_completion(student):
    score = 0

    if student["lessons_completed"] > 50:
        score += 40
    if student["login_frequency"] > 3:
        score += 30
    if student["assignments_done"]:
        score += 30

    return {
        "completion_probability": min(score, 100),
        "risk": "high" if score < 40 else "low"
    }
