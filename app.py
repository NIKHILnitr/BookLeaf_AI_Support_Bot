import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from supabase import create_client
import os
import pandas as pd
from datetime import datetime

# Load environment variables
load_dotenv(override=True)

# Environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Initialize clients
client = Groq(api_key=groq_api_key)
supabase = create_client(supabase_url, supabase_key)

# UI
st.title("BookLeaf AI Support Bot")
st.write("Ask publishing-related questions below.")

query = st.text_input("Ask your question")

if query:

    try:
        # Fetch author data
        data = supabase.table("authors").select("*").execute()

        authors = data.data

        # Handle empty DB
        if not authors:
            st.warning("No author records found.")
            st.stop()

        # Create database context
        context = "\n".join([
            f"""
            Email: {a.get('email')}
            Book Title: {a.get('book_title')}
            Final Submission Date: {a.get('final_submission_date')}
            Book Live Date: {a.get('book_live_date')}
            Royalty Status: {a.get('royalty_status')}
            ISBN: {a.get('isbn')}
            Add-On Services: {a.get('add_on_services')}
            """
            for a in authors
        ])

        # AI Prompt
        prompt = f"""
        You are BookLeaf's AI support assistant.

        Use ONLY the database information below to answer.

        If confidence is low or answer is unclear,
        respond exactly with:
        "Escalating this query to a human support agent."

        DATABASE:
        {context}

        USER QUESTION:
        {query}
        """

        # Generate AI response
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="openai/gpt-oss-120b",
        )

        answer = response.choices[0].message.content

        # Show response
        st.success(answer)

        # Logging
        log = pd.DataFrame({
            "timestamp": [datetime.now()],
            "query": [query],
            "response": [answer]
        })

        if os.path.exists("query_logs.csv"):
            log.to_csv("query_logs.csv", mode="a", header=False, index=False)
        else:
            log.to_csv("query_logs.csv", index=False)

    except Exception as e:
        st.error(f"System Error: {e}")