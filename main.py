from agent.controller import CustomerResolutionAgent

if __name__ == "__main__":
    agent = CustomerResolutionAgent(order_id="ORD-9921")
    final_state = agent.run()

    print("\n==========================================")
    print("FINAL RESOLUTION STATE SUMMARY")
    print("==========================================")
    print(f"Status: {final_state['status']}")
    print(f"Total Workflow Steps Executed: {len(final_state['history'])}")
