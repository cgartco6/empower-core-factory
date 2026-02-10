GDPR_RULES = {
    "lawful_basis": ["consent", "contract", "legal obligation"],
    "rights": [
        "right to access",
        "right to rectification",
        "right to erasure",
        "right to portability"
    ],
    "disclosures": [
        "data retention",
        "third-party sharing",
        "international transfers"
    ]
}

def validate_gdpr(doc):
    errors = []

    text = doc["content"].lower()

    for basis in GDPR_RULES["lawful_basis"]:
        if basis not in text:
            errors.append(f"Missing lawful basis: {basis}")

    for right in GDPR_RULES["rights"]:
        if right not in text:
            errors.append(f"Missing GDPR right: {right}")

    for item in GDPR_RULES["disclosures"]:
        if item not in text:
            errors.append(f"Missing disclosure: {item}")

    return errors
