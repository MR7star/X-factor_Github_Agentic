# Simulated enterprise databases and external tool APIs

MOCK_ORDERS = {
    "ORD-9921": {
        "customer_id": "CUST-101",
        "item_id": "ITEM-55",
        "item_name": "Wireless Headphones",
        "price": 120.00,
        "status": "DELIVERED",
        "return_eligible": True,
    }
}

MOCK_INVENTORY = {
    "ITEM-55": 0  # Trigger failure scenario: Item is OUT OF STOCK
}

MOCK_CUSTOMER_ACCOUNTS = {
    "CUST-101": {"name": "Alex Mercer", "tier": "VIP", "balance": 0.00}
}


def get_order_details(order_id: str) -> dict:
    return MOCK_ORDERS.get(order_id, {"error": "Order not found"})


def check_inventory(item_id: str) -> dict:
    stock = MOCK_INVENTORY.get(item_id, 0)
    return {"item_id": item_id, "stock": stock, "available": stock > 0}


def execute_replacement(order_id: str, item_id: str) -> dict:
    inventory = check_inventory(item_id)
    if not inventory.get("available"):
        return {
            "status": "FAILED",
            "reason": f"Replacement item {item_id} is OUT OF STOCK.",
        }
    return {"status": "SUCCESS", "action": "REPLACEMENT_ISSUED", "order_id": order_id}


def execute_refund(order_id: str, amount: float) -> dict:
    order = MOCK_ORDERS.get(order_id)
    if not order:
        return {"status": "FAILED", "reason": "Invalid order"}

    cust_id = order["customer_id"]
    MOCK_CUSTOMER_ACCOUNTS[cust_id]["balance"] += amount
    MOCK_ORDERS[order_id]["status"] = "REFUNDED"

    return {
        "status": "SUCCESS",
        "action": "REFUND_ISSUED",
        "amount_refunded": amount,
        "new_customer_balance": MOCK_CUSTOMER_ACCOUNTS[cust_id]["balance"],
    }
