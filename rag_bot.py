import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Enterprise RAG Bot", page_icon="🤖", layout="centered")
st.title("🤖 RAG Company Chatbot")
st.markdown("Paste a company URL. The AI will scrape the DOM, read the data, and let you chat with the website.")

# --- 2. AI SETUP ---
# PASTE YOUR API KEY HERE
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-3-flash-preview')

# --- 3. THE MEMORY (Session State) ---
# Streamlit refreshes the page every time you click a button.
# We use 'session_state' as a temporary cache so the AI doesn't forget the website text.
if "scraped_text" not in st.session_state:
    st.session_state.scraped_text = ""

# --- 4. THE UI & EXTRACTION PIPELINE ---
url_input = st.text_input("🔗 Enter Target URL (e.g., https://example.com):")

if st.button("📡 Extract Website Data"):
    if not url_input:
        st.warning("⚠️ Please enter a URL first.")
    else:
        with st.spinner("Bypassing firewall and extracting DOM text..."):
            try:
                # The browser disguise
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(url_input, headers=headers)
                
                # Check for 403 or 404 errors
                if response.status_code != 200:
                    st.error(f"❌ Access Denied by Server (Status {response.status_code})")
                else:
                    # Parse the DOM
                    soup = BeautifulSoup(response.content, "html.parser")
                    
                    # Target all <p> (paragraph) tags to get the readable text
                    paragraphs = soup.find_all('p')
                    
                    # Combine all paragraphs into one giant string
                    extracted_text = " ".join([p.text for p in paragraphs])
                    
                    # Save to memory (limit to 5000 characters so we don't crash the free API)
                    st.session_state.scraped_text = extracted_text[:5000]
                    
                    st.success("✅ DOM Extracted! The AI has ingested the company data.")
            except Exception as e:
                st.error(f"❌ Network Error: {e}")

# --- 5. THE RAG CHAT INTERFACE ---
# Only show the chat box IF we have successfully scraped data
if st.session_state.scraped_text:
    st.markdown("---")
    st.markdown("### 💬 Chat with the Website")
    
    user_question = st.text_input("Ask a question about this company:")
    
    if st.button("Ask AI"):
        if user_question:
            with st.spinner("Analyzing extracted data..."):
                
                # THE RAG PROMPT (Forcing the AI to ONLY use the scraped data)
                prompt = f"""
                You are a corporate AI assistant. Answer the user's question based ONLY on the following scraped website data. 
                If the answer is not in the data, do not guess. Simply say "I cannot find this in the provided company data."
                
                --- SCRAPED WEBSITE DATA ---
                {st.session_state.scraped_text}
                
                --- USER QUESTION ---
                {user_question}
                """
                
                try:
                    response = model.generate_content(prompt)
                    st.info(response.text)
                except Exception as e:
                    st.error(f"❌ API Error: {e}")