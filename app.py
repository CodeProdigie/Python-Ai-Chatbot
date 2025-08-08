import streamlit as st
import google.generativeai as genai

# --- Gemini API Setup ---
st.set_page_config(page_title="Virus Detected", page_icon="🤖")

st.title("🤖 Virus Detected")
st.caption("Powered by Google's Gemini API + Streamlit")

# Input your Gemini API key securely
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")



if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")


    # Initialize chat session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for role, text in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(text)

    # User input
    prompt = st.chat_input("Ask something...")

    if prompt:
        # Add user message
        st.session_state.chat_history.append(("user", prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gemini API call
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                response = model.generate_content(prompt)
                reply = response.text
            except Exception as e:
                reply = f"⚠️ Error: {e}"

            message_placeholder.markdown(reply)

        # Add assistant response
        st.session_state.chat_history.append(("assistant", reply))
else:
    st.warning("Please enter your Gemini API key to start chatting.")



