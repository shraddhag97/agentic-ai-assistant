import streamlit as st
from agent import run_agent

st.title("Agentic AI Research Assistant")

topic = st.text_input("Enter research topic:")

if st.button("Run Research"):

    if not topic:
        st.warning("Please enter a topic")
        st.stop()

    with st.spinner("Agent researching..."):
        report = run_agent(topic)

    st.subheader("Research Report")
    st.write(report)
    st.divider()
    st.caption("Generated using live web research by agent")