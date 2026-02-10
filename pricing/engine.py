def calculate_total(cart):
    subtotal = sum(i["price"] * i["qty"] for i in cart["items"])

    discount = 0
    if cart.get("coupon") == "MOMPOWER":
        discount = subtotal * 0.15

    tax = subtotal * 0.15  # configurable per country

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": subtotal - discount + tax
    }
