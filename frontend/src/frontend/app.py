import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000/JUAI/ask"

# Create empty list for chat-history.
def init_session_states():
    if "messages" not in st.session_state: 
        st.session_state.messages = []

# Creates all previous messages and answers as chat bubbles.
# Necessary because streamlit reruns the whole script.
def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Receives a new question, sends it to backend and displays the answer.
def handle_user_input():
    # The square of text at the bottom. Only runs if user-input.
    if prompt := st.chat_input("Ställ en fråga om avdrag i tjänst"):
        # Displays the question and stores in history.
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Send question in same format as Prompt in data_models.py.
        response = requests.post(BASE_URL, json={"prompt": prompt}, timeout=60)
        if response.status_code != 200:
            st.error(f"Något gick fel ({response.status_code}), försök igen.")
            return
        else:
            # Answer has same fields as RagResponse in data_models.py.
            data = response.json()
            answer = (
                f"{data['answer']}\n\n"
                f"**Källa:** 12 kap. {data['paragraph_nr']} § - {data['title']}"
            )
        # Display answer and store in history.
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
            

def layout():
    st.markdown("# JUAI")
    st.markdown("Ställ en fråga om avdrag i inkomstslaget tjänst (12 kap. inkomstskattelagen)")
    st.caption("Disclaimer: Detta är inte skatterådgivning")

    display_chat_messages()
    handle_user_input()

# Runs when app starts with streamlit run.
# History must exist before layout() tries to display it.
if __name__ == "__main__":
    init_session_states()
    layout()