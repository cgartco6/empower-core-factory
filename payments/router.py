def payment_methods(country):
    if country == "ZA":
        return ["EFT", "PayFast", "PayShap", "Crypto"]
    return ["Stripe", "PayPal", "Crypto"]
