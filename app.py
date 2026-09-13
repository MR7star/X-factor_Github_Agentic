import streamlit as st
import json
from agent.controller import CustomerResolutionAgent

st.set_page_config(page_title="Autonomous Resolution Agent", layout="wide")

st.title("Autonomous Customer Resolution Agent")
st.caption("Track 3 — Problem Statement 5: Enterprise Resolution Loop")

# Sidebar - Input details
st.sidebar.header("Customer Issue Setup")
order_id = st.sidebar.text_input("Order ID", value="ORD-9921")
issue_desc = st.sidebar.selectbox("Customer Issue", ["Item Damaged - Request Replacement", "Order Cancellation", "Wrong Item Delivered"])

if st.sidebar.button("Run Resolution Agent", type="primary"):
    st.subheader(f"Processing Order: {order_id}")
    
    # Initialize Agent
    agent = CustomerResolutionAgent(order_id=order_id)
    
    # Run Agent Loop
    with st.spinner("Agent evaluating policy, calling enterprise APIs, and handling exceptions..."):
        final_state = agent.run()
    
    # Display Results & State Log
    st.success("Workflow Complete!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Agent Action Log & Adaptation Trail")
        for step in final_state["history"]:
            step_name = step["step"].replace("_", " ").title()
            with st.expander(f"Step: {step_name}", expanded=True):
                st.json(step["result"])
    
    with col2:
        st.subheader("Final System State")
        st.metric(label="Workflow Status", value=final_state["status"])
        st.metric(label="Steps Executed", value=len(final_state["history"]))