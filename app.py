import streamlit as st
import csv
import google.generativeai as genai

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="AI Resume Matcher", page_icon="🎯", layout="centered")

st.title("🎯 AI Resume Matcher")
st.markdown("This tool cross-references your resume against live scraped market data to find your top 3 job matches.")

# --- 2. THE AI SETUP ---
# PASTE YOUR API KEY HERE
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-3-flash-preview')

# --- 3. THE USER INTERFACE ---
# Instead of hardcoding the resume, we give the user a clean text box to paste it in
resume_input = st.text_area("Paste your Resume / Skills here:", height=200, placeholder="E.g. I am a Computer Science student skilled in Python, Next.js, and data extraction...")

# A sleek button to trigger the pipeline
if st.button("🚀 Analyze Market Matches"):
    
    if not resume_input.strip():
        st.warning("⚠️ Please paste your resume first!")
    else:
        # A loading spinner so the user knows the AI is thinking
        with st.spinner("Extracting data and consulting AI..."):
            
            # --- 4. THE DATA PIPELINE ---
            jobs_list = []
            try:
                with open('market_data.csv', 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader) # Skip header
                    for row in reader:
                        jobs_list.append(f"{row[0]} at {row[1]}")
                
                jobs_text = "\n".join(jobs_list[:15]) # Grab first 15 for speed

                # --- 5. THE AI PROMPT ---
                prompt = f"""
                Act as an expert Tech Recruiter. Here is the candidate's resume:
                {resume_input}

                Here is a list of open tech jobs scraped from the market:
                {jobs_text}

                Based strictly on the resume, pick the top 3 jobs from the list they are most qualified for.
                Format the output as a clean, numbered list. For each job, give a one-sentence explanation of why it is a match.
                """

                # --- 6. THE OUTPUT ---
                response = model.generate_content(prompt)
                
                st.success("✅ Analysis Complete!")
                
                # We use markdown to make the AI's bold text look great on the web page
                st.markdown("### Top Recommended Roles")
                st.markdown(response.text)

            except FileNotFoundError:
                st.error("❌ Error: market_data.csv not found! Run your scraper first.")
            except Exception as e:
                st.error(f"❌ API Error: {e} (Did you paste your API key?)")