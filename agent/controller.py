import json
from tools.enterprise_db import (
    get_order_details,
    check_inventory,
    execute_replacement,
    execute_refund,
)
from tools.policy_rules import query_policy_rag
from tools.verification import verify_resolution


class CustomerResolutionAgent:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.state = {
            "order_id": order_id,
            "history": [],
            "status": "IN_PROGRESS",
            "current_plan": "Attempt replacement, fallback to refund if unavailable.",
        }

    def log_step(self, step_name: str, result: dict):
        self.state["history"].append({"step": step_name, "result": result})
        print(f"\n[AGENT LOG - {step_name.upper()}]")
        print(json.dumps(result, indent=2))

    def run(self):
        print(f"=== Starting Autonomous Resolution Loop for Order {self.order_id} ===")

        # Step 1: Retrieve Order State
        order_info = get_order_details(self.order_id)
        self.log_step("1_fetch_order_info", order_info)

        # Step 2: Query Policy Knowledge Base
        policy = query_policy_rag("replacement")
        self.log_step("2_check_policy", {"policy": policy})

        # Step 3: Action Execution Attempt (Replacement)
        item_id = order_info["item_id"]
        replacement_result = execute_replacement(self.order_id, item_id)
        self.log_step("3_attempt_replacement", replacement_result)

        # Step 4: Detect Action Failure & Adapt Dynamically
        if replacement_result.get("status") == "FAILED":
            print("\n ACTION BLOCKED: Replacement item is out of stock.")
            print("ADAPTATION LOOP: Consulting out-of-stock policy and replanning...")

            fallback_policy = query_policy_rag("out_of_stock")
            self.log_step("4_replanning_policy_check", {"policy": fallback_policy})

            # Execute Alternative Action (Refund)
            refund_amount = order_info["price"]
            refund_result = execute_refund(self.order_id, refund_amount)
            self.log_step("5_execute_fallback_refund", refund_result)

            # Step 5: Verification Phase
            verification = verify_resolution(self.order_id, expected_action="REFUND")
            self.log_step("6_verify_final_outcome", verification)

            self.state["status"] = "COMPLETED"
            return self.state
        else:
            verification = verify_resolution(
                self.order_id, expected_action="REPLACEMENT"
            )
            self.log_step("4_verify_outcome", verification)
            self.state["status"] = "COMPLETED"
            return self.state
