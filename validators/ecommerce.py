def validate_cart(cart):
    errors = []

    if not cart["items"]:
        errors.append("Cart empty")

    for item in cart["items"]:
        if item["price"] < 0:
            errors.append("Negative price detected")
        if item["qty"] <= 0:
            errors.append("Invalid quantity")

    return errors
