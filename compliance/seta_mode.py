def apply_seta_rules(course):
    course["locked"] = True
    course["versioned"] = True
    course["audit_required"] = True
    course["attendance_required"] = True
    return course
