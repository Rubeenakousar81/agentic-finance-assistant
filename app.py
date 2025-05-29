import streamlit as st
from agents.api_agent import api_agent
from agents.language_agent import generate_summary

st.title("🧠 Morning Market Brief")
query = st.text_input("Ask your question:")

if query:
    summary = generate_summary(query, retriever=None)  # Replace with actual retriever
    st.write(summary)
