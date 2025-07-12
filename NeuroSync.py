# Project: NeuroSync 🤖🧠
# An AI-Powered Resume Chatbot That Knows You Better Than Your Boss

# --- SETUP ---
import os
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

# 🌐 Load OpenAI API key from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# --- LOAD RESUME ---
print("🚀 Loading your resume into NeuroSync's neural matrix...")
loader = PyPDFLoader("your_resume.pdf")  # Make sure your resume is named exactly
pages = loader.load()

# --- SPLIT & EMBED ---
print("🧬 Chunking and embedding your data...")
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
doc_chunks = splitter.split_documents(pages)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(doc_chunks, embeddings)

# --- BUILD CHATBOT CHAIN ---
print("🤖 Activating NeuroSync...")
qa_bot = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0.3),
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# --- INTERACTIVE CHAT LOOP ---
print("💬 NeuroSync is online. Ask me anything about yourself!")
while True:
    query = input("\nYou > ")
    if query.lower() in ["exit", "quit"]:
        print("🛑 Shutting down NeuroSync. See you in the metaverse!")
        break
    response = qa_bot({"query": query})
    print("NeuroSync >", response['result'])
