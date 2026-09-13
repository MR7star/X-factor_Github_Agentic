from tools.enterprise_db import MOCK_ORDERS, MOCK_CUSTOMER_ACCOUNTS


def verify_resolution(order_id: str, expected_action: str) -> dict:
    order = MOCK_ORDERS.get(order_id, {})
    cust_id = order.get("customer_id")
    account = MOCK_CUSTOMER_ACCOUNTS.get(cust_id, {})

    if expected_action == "REFUND" and order.get("status") == "REFUNDED":
        return {
            "verified": True,
            "details": f"Verified: Order {order_id} status updated to REFUNDED. Account balance updated to ${account.get('balance')}.",
        }
    return {"verified": False, "details": "Resolution state could not be verified."}
