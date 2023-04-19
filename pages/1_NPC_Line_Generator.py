import streamlit as st
import openai

st.title("NPC Line Generator")

if "history" not in st.session_state:
    st.session_state.history = []

def submit():
    npc_description = st.session_state.npc_description
    prompt = (
        "You are a character in a game interacting with a player. Say something as the character.\n"
        f"{'Here is a description of your character: ' if npc_description else ''}"
        f"{npc_description}"
    )

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return result["choices"][0]["message"]["content"]

if "api_token" in st.session_state:
    openai.api_key = st.session_state.api_token

    form = st.form("npc-line")
    form.text_area("Describe the NPC (Optional)", key="npc_description")
    submit_button = form.form_submit_button("Submit")

    if submit_button:
        result = submit()
        st.session_state.history.append(result)

    for i, line in enumerate(reversed(st.session_state.history)):
        if i == 0:
            st.markdown(f"**{line}**")
        else:
            st.markdown(line)
else:
    st.error("Please enter an OpenAI API Token on the About page to use this tool.")
