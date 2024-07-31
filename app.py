import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text_data = []
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        pdf_name = pdf.name
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            if text:
                text_data.append({
                    "text": text,
                    "page_num": page_num + 1,  # page numbers start from 1
                    "pdf_name": pdf_name
                })
    return text_data

def get_text_chunks(text_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = []
    for data in text_data:
        text_chunks = text_splitter.split_text(data["text"])
        for chunk in text_chunks:
            chunks.append({
                "text": chunk,
                "page_num": data["page_num"],
                "pdf_name": data["pdf_name"]
            })
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    texts = [chunk["text"] for chunk in text_chunks]
    metadata = [{"page_num": chunk["page_num"], "pdf_name": chunk["pdf_name"]} for chunk in text_chunks]
    vector_store = FAISS.from_texts(texts, embedding=embeddings, metadatas=metadata)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question using the provided context in a detailed and well-structured manner. Include all relevant information and specify the page numbers, line numbers, and PDF names where the information is found. If the answer is not in the provided context, simply state, "The answer is not available in the context." Do not provide incorrect information.

    Context:\n{context}\n
    Question:\n{question}\n

    Answer:
    - Introduction: Briefly introduce the topic.
    - Details: Provide detailed information based on the context.
    - Conclusion: Summarize the key points.
    - References: List the page numbers, line numbers, and PDF names.
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )

    detailed_response = response["output_text"]
    
    st.write("Reply: ", detailed_response)
    
    # Display metadata
    for doc in docs:
        st.write(f"Context found in: PDF Name: {doc.metadata['pdf_name']}, Page Number: {doc.metadata['page_num']}")

def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini 😎")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
