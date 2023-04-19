import streamlit as st
import openai

st.title("NPC Chat")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

def submit():
    st.session_state.conversation.append({"role": "user", "content": st.session_state.user_input})

    npc_description = st.session_state.chat_npc_description
    prompt = (
        "You are a character in a game interacting with a player.\n"
        f"{'Here is a description of your character: ' if npc_description else ''}"
        f"{npc_description}"
    )
    conversation = [{"role": "system", "content": prompt}] + st.session_state.conversation
    
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    st.session_state.conversation.append({"role": "assistant", "content": result["choices"][0]["message"]["content"]})
    st.session_state.user_input = ""

def reset():
    st.session_state.conversation = []

if "api_token" in st.session_state:
    openai.api_key = st.session_state.api_token

    settings, chat = st.columns(2)

    with settings:
        form = st.form("npc-chat-settings")
        form.text_area("Describe the NPC (Optional)", key="chat_npc_description")
        form.form_submit_button("Submit")

    with chat:
        for turn in st.session_state.conversation:
            st.write(f"{'User' if turn['role'] == 'user' else 'NPC'}: {turn['content']}")

        st.text_input("User Input", on_change=submit, label_visibility="hidden", key="user_input")
        st.button("Reset Conversation", on_click=reset)
else:
    st.error("Please enter an OpenAI API Token on the About page to use this tool.")
