# AI & Data Extraction Pipelines 🚀

This repository contains a collection of Python-based data engineering and AI integration tools built to extract unstructured web data and process it using Large Language Models (LLMs).

## 📂 Project Architecture

### 1. Market Data Web Scraper (`scraper.py`)
An automated HTTP pipeline that acts as a headless browser to bypass basic server protections, parse live DOM elements via `BeautifulSoup`, and structure raw market data into a clean CSV format.

### 2. AI Resume Matcher (`app.py`)
A Streamlit web application that ingests the scraped CSV data and cross-references it against a user's skills using the **Google Gemini API**. It processes the data arrays and forces the LLM to output a deterministic, formatted business decision.

### 3. Enterprise RAG Chatbot (`rag_bot.py`)
A Retrieval-Augmented Generation (RAG) tool. Users input a target URL, and the script extracts the DOM `<p>` tags into temporary session memory. The Gemini API is then restricted to *only* answer user queries based on the ingested, private company data. 

## 🛠️ Tech Stack
* **Language:** Python
* **Data Extraction:** `requests`, `BeautifulSoup4`
* **AI Integration:** Google Generative AI SDK (Gemini Pro)
* **Frontend UI:** Streamlit

---

## ⚙️ How to Run Locally

### Prerequisites
1. Ensure **Python 3.8+** is installed on your machine.
2. Obtain a free **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Step 1: Install Dependencies
Open your terminal and run the following command to install the required libraries:
`pip install requests beautifulsoup4 streamlit google-generativeai`

### Step 2: Configure API Keys
Before running the AI applications, open `app.py` and `rag_bot.py` in your code editor. Locate the API configuration line and paste your Gemini API key inside the quotes:
`genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")`

### Step 3: Execute the Projects

**1. Generate the Dataset (Web Scraper)**
You must run this script first to extract the live web data and generate the `market_data.csv` file that the AI will read.
`python scraper.py`

**2. Launch the AI Resume Matcher**
This command will spin up a local web server and open the application UI in your browser.
`streamlit run app.py`

**3. Launch the RAG Chatbot**
This command will launch the web-based chatbot interface, ready to ingest and analyze live URLs.
`streamlit run rag_bot.py`
