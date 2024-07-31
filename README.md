# LearnSmart 😎

This Streamlit application allows you to upload PDF files, process their text, and interact with the content using natural language queries powered by Google Gemini AI.

## Features

- **Upload PDF Files**: Upload multiple PDF files and process them to extract text.
- **Text Chunking**: Automatically splits the extracted text into manageable chunks for better processing.
- **Vector Store Creation**: Uses Google Generative AI embeddings to create a vector store for efficient similarity searches.
- **Conversational Chain**: Utilizes Google Gemini AI to answer questions based on the content of the uploaded PDFs.
- **Interactive UI**: Simple and user-friendly interface to interact with your PDFs.

## Installation

### Prerequisites

- Python 3.7+

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KandarpJoshi1112/Learn-Smart
   cd Learn-Smart
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root of your project and add your Google API key:

   ```env
   GOOGLE_API_KEY=your-google-api-key
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Upload PDFs:**

   - Use the sidebar to upload multiple PDF files.
   - Click on the "Submit & Process" button to extract and process the text from the PDFs.

3. **Ask Questions:**

   - Enter your question in the text input field and press Enter.
   - The application will use the content of the uploaded PDFs to answer your question.

## How It Works

1. **PDF Text Extraction:**

   The `get_pdf_text` function extracts text from the uploaded PDF files.

2. **Text Chunking:**

   The `get_text_chunks` function splits the extracted text into smaller chunks using `RecursiveCharacterTextSplitter`.

3. **Vector Store Creation:**

   The `get_vector_store` function creates a vector store from the text chunks using Google Generative AI embeddings and FAISS.

4. **Conversational Chain:**

   The `get_conversational_chain` function sets up a QA chain using Google Gemini AI to answer questions based on the processed PDF content.

5. **User Input Handling:**

   The `user_input` function processes the user's question, performs a similarity search on the vector store, and retrieves the most relevant chunks to generate an answer.

## Example

1. **Upload PDFs:** Use the sidebar to upload your PDF files.
2. **Ask a Question:** Enter a question like "What is the main topic of the document?" in the input field.
3. **Get an Answer:** The app will display a detailed answer based on the content of the uploaded PDFs.

---

Enjoy chatting with your PDFs using LearnSmart! 🚀

## Requirements

Here is the content for your `requirements.txt` file:

```text
streamlit
google-generativeai
python-dotenv
langchain
PyPDF2
chromadb
faiss-cpu
langchain_google_genai
```

## Environment Variables

Replace the API key in  `env.example` file and rename it to `.env`:

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

---

## Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Generative AI](https://img.shields.io/badge/Google%20Generative%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-0E76A8?style=for-the-badge&logo=langchain&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-4A148C?style=for-the-badge&logo=database&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-0E76A8?style=for-the-badge&logo=faiss&logoColor=white)
![dotenv](https://img.shields.io/badge/dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)
