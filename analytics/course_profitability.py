def score_course(course):
    revenue = course["sales"] * course["price"]
    cost = (
        course["ai_cost"] +
        course["marketing_cost"] +
        course["support_cost"]
    )

    margin = revenue - cost
    roi = (margin / cost) if cost > 0 else 0

    score = 0
    if roi > 2:
        score += 40
    if course["completion_rate"] > 60:
        score += 30
    if course["refund_rate"] < 5:
        score += 20
    if course["conversion_rate"] > 3:
        score += 10

    return {
        "course": course["name"],
        "roi": round(roi, 2),
        "profit": margin,
        "score": score,
        "decision": (
            "scale" if score > 70 else
            "optimize" if score > 40 else
            "sunset"
        )
    }
