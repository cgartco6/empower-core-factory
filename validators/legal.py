def validate_legal(doc):
    required = ["Privacy", "Data", "User", "Rights"]
    errors = []

    for word in required:
        if word not in doc["content"]:
            errors.append(f"Missing legal term: {word}")

    return errors
