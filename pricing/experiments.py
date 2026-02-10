def generate_price_variants(base_price):
    return [
        round(base_price * 0.9, 2),
        base_price,
        round(base_price * 1.1, 2)
    ]

def evaluate_pricing(results):
    best = max(results, key=lambda x: x["revenue"])
    return {
        "winner_price": best["price"],
        "confidence": best["revenue"] / sum(r["revenue"] for r in results)
    }
