import streamlit as st
from retriever import get_relevant_docs
from generator import generate_answer

st.title("🤖 Tonton FAQ Chatbot")

query = st.text_input("Tanya soalan anda di sini...")

if query:
    with st.spinner("Thinking..."):
        docs = get_relevant_docs(query)
        context ="\n\n".join([doc.page_content for doc in docs])
        answer = generate_answer(query, context)
    
    st.success("Done!")
    st.write("### 🤖 Answer:")
    st.markdown(f"**Jawapan:** {answer}")
