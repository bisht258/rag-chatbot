# 📄 RAG Chatbot — Ask Questions from PDF

An AI-powered chatbot that allows users to upload a PDF document and ask questions about its content.

The app extracts text, performs semantic search, and generates accurate answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

✔ Upload any PDF document
✔ Extract and process document text
✔ Smart chunking & semantic search
✔ AI answers based only on document content
✔ Streamlit-based interactive UI
✔ Prevents hallucinations using context grounding

---

## 🧠 How It Works

1. PDF is uploaded by the user
2. Text is extracted using **pdfplumber**
3. Text is split into chunks
4. Embeddings convert text into vectors
5. FAISS performs similarity search
6. Relevant context is sent to the AI model
7. AI generates an accurate answer

This process is called **Retrieval-Augmented Generation (RAG)**.

---

## 🖥️ Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI Embeddings & LLM
* FAISS Vector Database
* pdfplumber

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/rag-chatbot.git
cd rag-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Set Your API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

OR set environment variable:

### Windows (PowerShell)

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

### Mac/Linux

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run ragchatbot.py
```

---

## 💬 How to Use

1. Upload a PDF file
2. Wait for processing
3. Ask questions about the document
4. Get AI-generated answers

---

## ⚠️ Notes

* The chatbot answers **only from the uploaded document**
* If the answer is not in the document, it will say so
* Works best with text-based PDFs

---

## 🌟 Future Improvements

* Chat history & conversation memory
* Support for multiple documents
* Deploy online for public access
* Use free local LLMs (Ollama)
* Add citations & source highlighting

---

## 👨‍💻 Author

**Vishal Bisht**
Aspiring Software Engineer & AI Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
