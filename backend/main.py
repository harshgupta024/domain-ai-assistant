from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

# -----------------------
# Load embeddings
# -----------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -----------------------
# Prompt template
# -----------------------
prompt = ChatPromptTemplate.from_template(
    """
    You are a domain-specific AI assistant.
    Answer ONLY from the provided context.
    If the answer is not present, say "I don't know".

    Context:
    {context}

    Question:
    {question}
    """
)

# -----------------------
# API schema
# -----------------------
class Question(BaseModel):
    question: str

# -----------------------
# Chat endpoint
# -----------------------
@app.post("/chat")
def chat(query: Question):
    # ✅ NEW LANGCHAIN API
    docs = retriever.invoke(query.question)

    context = "\n\n".join(d.page_content for d in docs)

    messages = prompt.format_messages(
        context=context,
        question=query.question
    )

    # Simple local response (domain-restricted)
    answer = context[:800] if context else "I don't know"

    return {"answer": answer}
