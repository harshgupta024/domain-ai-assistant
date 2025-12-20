import streamlit as st
import requests

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Domain AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("📘 Domain AI Assistant")
st.sidebar.markdown(
    """
    **Project:** Domain-Specific AI Knowledge Assistant  
    **Technology:** RAG + Vector Search  
    **Backend:** FastAPI  
    **Vector DB:** FAISS  

    ---
    Ask questions strictly based on the uploaded domain documents.
    """
)

st.sidebar.info("⚠️ Answers are generated only from the dataset.")

# -------------------------
# Main UI
# -------------------------
st.title("🤖 Domain-Specific AI Knowledge Assistant")
st.caption("Powered by Vector Search & Retrieval Augmented Generation (RAG)")

API_URL = "https://domain-ai-assistant-backend.onrender.com/chat"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask a question from the document...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    try:
        response = requests.post(
            API_URL,
            json={"question": user_input},
            timeout=60
        )
        answer = response.json()["answer"]
    except Exception as e:
        answer = "❌ Backend not reachable. Please ensure FastAPI is running."

    # Display assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
