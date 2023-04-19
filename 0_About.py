import streamlit as st

def submit():
    st.session_state.api_token = st.session_state.token
    st.success("OpenAI API Token Entered")

if "api_token" in st.session_state:
    if "token" not in st.session_state:
        st.success("OpenAI API Token Entered")
    input_text = "Change OpenAI API Token"
    placeholder = st.session_state.api_token
else:
    input_text = "Enter OpenAI API Token"
    placeholder = None

token = st.text_input(input_text, on_change=submit, key="token", placeholder=placeholder)
