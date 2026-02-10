def revenue_insights(orders):
    total = sum(o["amount"] for o in orders)

    by_course = {}
    for o in orders:
        by_course[o["course"]] = by_course.get(o["course"], 0) + o["amount"]

    top_course = max(by_course, key=by_course.get)

    return {
        "total_revenue": total,
        "top_course": top_course,
        "revenue_by_course": by_course
    }
