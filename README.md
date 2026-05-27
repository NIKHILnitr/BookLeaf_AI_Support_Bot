# 📚 BookLeaf AI Support Bot

AI-powered customer support bot for publishing workflows using Streamlit, Supabase, and Groq LLM.

---

## 🚀 Features

- Supabase database integration (author book records)
- AI-powered responses using Groq LLM (Llama3)
- Knowledge Base support for publishing FAQs
- Human escalation for low-confidence queries
- Query logging system (CSV)
- Chat-style UI using Streamlit
- Basic identity-aware query handling concept

---

## 🎥 Project Demo (Loom Video)
👉 https://www.loom.com/share/49c2aaa6d8d946928902fc310150210f

---

## 🏗️ Tech Stack

- Python
- Streamlit
- Supabase
- Groq API
- Pandas
- python-dotenv

---


## ⚙️ Setup Instructions

### 1. Install dependencies

pip install -r requirements.txt


---

### 2. Create `.env` file

GROQ_API_KEY=your_groq_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key


---

### 3. Run application

streamlit run app.py


---

## 🗄️ Database Schema (Supabase)

Table: `authors`

Columns:
- email
- book_title
- final_submission_date
- book_live_date
- royalty_status
- isbn
- add_on_services

---

## 🧪 Example Queries

- What is Sara’s royalty status?
- Is my book live yet?
- When are royalty reports generated?
- What add-on services does Emily have?

---

## ⚡ System Flow

User Query → Streamlit UI → Groq LLM → Supabase + Knowledge Base → Response → Logging

---

## 🚨 Features Logic

- If query matches DB → fetch Supabase data
- If general question → use Knowledge Base
- If low confidence → escalate to human agent
- All queries saved in CSV log

---

## 📈 Future Improvements

- Add vector search (embeddings)
- WhatsApp / Instagram integration
- Identity unification system
- Dashboard analytics
- Role-based access control (RLS)

---

## 👨‍💻 Author


Nikhil Bhoi

