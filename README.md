# 📘 Domain-Specific AI Knowledge Assistant

## 📌 Project Overview

The **Domain-Specific AI Knowledge Assistant** is an AI-powered application designed to answer user queries strictly based on a predefined set of domain documents. The system leverages **Vector Search** and **Retrieval Augmented Generation (RAG)** to ensure responses are accurate, contextual, and grounded in the provided dataset.

This project demonstrates a complete end-to-end AI/ML workflow, including document ingestion, semantic search, backend API development, and an interactive frontend interface.

---

## 🎯 Objective

Traditional AI chatbots may generate hallucinated or irrelevant answers. This project addresses that issue by:
- Restricting responses to domain-specific documents
- Using semantic similarity instead of keyword-based search
- Providing reliable and explainable answers

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Frontend Framework:** Streamlit  
- **Vector Database:** FAISS  
- **Embeddings Model:** Sentence Transformers (all-MiniLM-L6-v2)  
- **AI Technique:** Retrieval Augmented Generation (RAG)

---

## 🧠 How the System Works

1. Domain documents (PDF) are loaded and split into smaller text chunks.
2. Each chunk is converted into numerical embeddings using a sentence transformer model.
3. These embeddings are stored in a FAISS vector database.
4. When a user asks a question:
   - The system retrieves the most relevant document chunks using vector similarity search.
   - The answer is generated strictly from the retrieved context.
5. The final response is displayed through an interactive chat interface.

---

## 📂 Project Structure

```
domain-ai-assistant/
│
├── backend/
│   ├── main.py                 # FastAPI backend
│   ├── ingest.py               # Document ingestion and vector creation
│   ├── requirements.txt
│
├── frontend/
│   ├── app.py                  # Streamlit user interface
│   ├── requirements.txt
│
├── data/
│   └── documents.pdf           # Domain-specific dataset
│
├── faiss_index/                # Stored vector embeddings
│
└── README.md
```

---

## ⚙️ Installation Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd domain-ai-assistant
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
```

**Activate (Windows):**
```bash
.\.venv\Scripts\activate
```

**Activate (macOS/Linux):**
```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
python -m pip install streamlit requests
```

---

## 📥 Dataset Setup

Place your domain-specific PDF file inside the following path:

```
data/documents.pdf
```

**Example domain used:**
- Artificial Intelligence and Machine Learning

---

## 🔁 Build Vector Index

Run the following command once to generate embeddings and store them in FAISS:

```bash
cd backend
python ingest.py
cd ..
```

---

## 🚀 Running the Application

### ▶️ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

**Backend URL:**
```
http://127.0.0.1:8000
```

**API documentation:**
```
http://127.0.0.1:8000/docs
```

### ▶️ Start Frontend (Streamlit)

Open a new terminal (with virtual environment activated):

```bash
python -m streamlit run frontend/app.py
```

**Frontend URL:**
```
http://localhost:8501
```

---

## 💬 How to Use the Application

1. Open the Streamlit web interface.
2. Enter a question related to the uploaded document.
3. The system retrieves relevant document context using vector search.
4. The assistant responds strictly based on the dataset.

**Example Queries:**
- What is artificial intelligence?
- Explain machine learning.
- What are the types of machine learning?
- What are the applications of AI?

---

## ✅ Key Features

- ✨ Domain-restricted question answering
- 🔍 Vector-based semantic search
- 🤖 Retrieval Augmented Generation (RAG)
- 💬 Interactive chat interface
- 🔒 Secure and modular backend
- 📴 Offline-friendly architecture

---

## 🔮 Future Enhancements

- [ ] Support for multiple document uploads
- [ ] Improved summarization models
- [ ] User authentication
- [ ] Cloud deployment
- [ ] Analytics and feedback system

---

## 👤 Author

**Harish Gupta**  
AI / ML Intern Candidate

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📧 Contact

For any queries or suggestions, please reach out via email or create an issue in the repository.