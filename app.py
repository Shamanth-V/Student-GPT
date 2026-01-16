import streamlit as st
from PyPDF2 import PdfReader

# Text splitting (older versions)
from langchain.text_splitter import RecursiveCharacterTextSplitter  # <- old style

# Vectorstore
from langchain.vectorstores import FAISS

# Embeddings (older style)
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# LLM (older style)
from langchain.llms.huggingface_endpoint import HuggingFaceEndpoint

# QA & memory
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

import os

# -----------------------------
# HuggingFace Config
# -----------------------------
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if HF_TOKEN is None:
    st.error("Set your HuggingFace token in the HUGGINGFACEHUB_API_TOKEN environment variable")
    st.stop()

INSTRUCTOR_MODEL = "hkunlp/instructor-xl"  # Free
LLM_MODEL = "hkunlp/instructor-xl"         # Free LLM for text-generation

# -----------------------------
# PDF Processing
# -----------------------------
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    """Simple text chunker without text_splitters"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks

def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name=INSTRUCTOR_MODEL,
        model_kwargs={"device": "cpu"},  # change to "cuda" if GPU available
        huggingfacehub_api_token=HF_TOKEN
    )
    return FAISS.from_texts(chunks, embeddings)

# -----------------------------
# QA Chain
# -----------------------------
def get_qa_chain(vectorstore):
    llm = HuggingFaceEndpoint(
        repo_id=LLM_MODEL,
        task="text-generation",
        temperature=0.3,
        max_new_tokens=200,
        huggingfacehub_api_token=HF_TOKEN
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        return_source_documents=False
    )

# -----------------------------
# Streamlit UI
# -----------------------------
def handle_userinput(question):
    if "qa_chain" not in st.session_state:
        st.error("Please upload and process PDFs first.")
        return

    response = st.session_state.qa_chain({"question": question})
    st.write(response["answer"])

def main():
    st.set_page_config(page_title="Ask Multiple PDFs", layout="wide")
    st.header("📄 Ask Multiple PDFs")

    question = st.text_input("Ask a question about your documents")
    if question:
        handle_userinput(question)

    with st.sidebar:
        st.subheader("Upload PDFs")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here",
            accept_multiple_files=True,
            type=["pdf"]
        )

        if st.button("Process PDFs"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF.")
                return
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                chunks = chunk_text(raw_text)
                vectorstore = get_vectorstore(chunks)
                st.session_state.qa_chain = get_qa_chain(vectorstore)
                st.success("PDFs processed successfully!")

if __name__ == "__main__":
    main()
