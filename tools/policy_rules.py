def query_policy_rag(topic: str) -> str:
    policies = {
        "replacement": "If a product is defective or damaged, offer a free replacement first if stock is available.",
        "out_of_stock": "If a replacement is requested but stock is unavailable, automatically offer a 100% full refund.",
        "refund_limit": "Full refunds can be processed up to $500 without manual managerial approval.",
    }
    return policies.get(topic, "Standard return and policy rules apply.")
