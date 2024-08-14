import streamlit as st
import google.generativeai as genai
import base64

st.title("I am your Real Estate Support Agent🌆🛬")
st.snow()
st.balloons()

if "memory" not in st.session_state:
    st.session_state["memory"] = []

@st.cache_data(persist=True)
def getImageAsBase64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

with open('key.txt') as f:
    key = f.read()

with open("conversation.txt") as f:
    instructions = f.read()

genai.configure(api_key=key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction=instructions
)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hii 🤖,  I'm here to help you"}
    ]
    st.title("I am Here to Clear Your Doubts")

# Add Font Awesome CDN link to the sidebar
st.sidebar.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# Sidebar content with buttons
st.sidebar.title("I am Dharunika")

st.sidebar.title("Contact 📞")
st.sidebar.markdown(
    """
    <style>

    </style>
    <a href="mailto:dharunikaramprakash@gmail.com" class="button"><i class="fas fa-envelope button-icon"></i>Email</a><br>
    <a href="tel:+916382875552" class="button"><i class="fas fa-phone button-icon"></i>Phone</a><br>
    <a href="https://github.com/Dharunikaramprakash/chatbot" target="_blank" class="button"><i class="fab fa-github button-icon"></i>GitHub</a><br>
    <a href="https://www.linkedin.com/in/dharunika-ramprakash-6b8413203/" target="_blank" class="button"><i class="fab fa-linkedin button-icon"></i>LinkedIn</a>
    """,
    unsafe_allow_html=True
)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input()

if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Loading..."):
                ai_response = model.generate_content(user_input)
                st.write(ai_response.text)
        new_ai_message = {"role": "assistant", "content": ai_response.text}
        st.session_state.messages.append(new_ai_message)
