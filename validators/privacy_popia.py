POPIA_RULES = [
    "data subject",
    "responsible party",
    "processing limitation",
    "purpose specification",
    "information security safeguards"
]

def validate_popia(doc):
    errors = []
    text = doc["content"].lower()

    for rule in POPIA_RULES:
        if rule not in text:
            errors.append(f"POPIA missing: {rule}")

    return errors
