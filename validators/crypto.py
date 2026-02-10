SUPPORTED_CRYPTO = ["BTC", "ETH", "USDT", "BNB", "SOL"]

def validate_crypto(payment):
    if payment["coin"] not in SUPPORTED_CRYPTO:
        raise Exception("Unsupported crypto")
