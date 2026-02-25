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
