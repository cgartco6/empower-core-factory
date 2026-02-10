def validate_course(course):
    errors = []
    if "Lesson" not in course["content"]:
        errors.append("No lesson structure")
    return errors
