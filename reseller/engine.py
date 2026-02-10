def reseller_split(order, reseller):
    platform_cut = order["amount"] * 0.3
    reseller_cut = order["amount"] * 0.7

    return {
        "platform": platform_cut,
        "reseller": reseller_cut,
        "reseller_id": reseller["id"]
    }
