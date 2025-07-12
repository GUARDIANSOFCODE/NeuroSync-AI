# 🧠 NeuroSync

> **"Plug your resume into the neural grid."**  
> An AI-powered personal chatbot that answers questions about your experience, education, and skills — like it *knows* you.

---

## 🚀 Overview

**NeuroSync** transforms your resume into an intelligent, interactive chatbot using OpenAI's GPT-4 and LangChain. Instead of just reading your CV, users can now ask questions like:

- "What programming languages do I know?"
- "Summarize my work experience."
- "What are my strengths from past projects?"

Whether you're a job seeker, recruiter, or tech enthusiast, NeuroSync is your next-gen resume interface.

---

## 🧠 How It Works

NeuroSync:
1. Loads your resume (PDF)
2. Breaks it into intelligent chunks
3. Embeds it into a vector database
4. Uses GPT-4 to retrieve and answer any question based on that data

All locally. All yours. No cloud storage. No compromise.

---

## 🛠️ Tech Stack

| Layer          | Tools Used                    |
|----------------|-------------------------------|
| Language Model | OpenAI GPT-4 (via API)        |
| Framework      | LangChain                     |
| Vector DB      | FAISS                         |
| Parsing        | PyPDFLoader                   |
| Language       | Python                        |
| Optional UI    | Streamlit (coming soon!)      |

---

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/NeuroSync.git
cd NeuroSync
