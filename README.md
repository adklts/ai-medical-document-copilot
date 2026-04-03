# AI Medical Document Copilot

An end-to-end AI-powered clinical document analysis system built with Retrieval-Augmented Generation (RAG) and a local LLM using Ollama.

## Features

- Upload medical documents (`.txt`, `.pdf`)
- Clean and preprocess text
- Split documents into chunks
- Generate embeddings with sentence-transformers
- Store and search vectors with FAISS
- Retrieve relevant context for a question
- Generate grounded answers with a local LLM
- Show evidence chunks in the UI
- Simple Streamlit interface

## Tech Stack

- Python
- Streamlit
- FAISS
- sentence-transformers
- Ollama (`llama3:8b`)
- PyMuPDF

## How It Works

-Upload a medical document
-Extract and clean text
-Split text into chunks
-Create embeddings
-Store embeddings in FAISS
-Retrieve relevant chunks for a user question
-Use a local LLM to generate a grounded answer
-Display the answer with evidence

## Installation

1. Clone the repository
git clone https://github.com/adklts/ai-medical-document-copilot.git
cd ai-medical-document-copilot
2. Install dependencies
pip install -r requirements.txt

## Install Ollama

Download and install Ollama, then run:

ollama run llama3:8b
Run the App
python -m streamlit run app/ui/streamlit_app.py**

## Example Questions
-What is the diagnosis?
-What symptoms are present?
-What treatment is recommended?
-What vital signs are recorded?
-Summarize the patient data.

## Notes

The system is designed to avoid hallucinations.
If information is missing, it should respond that it is not available in the document.
Best results depend on the type and quality of the uploaded data.

## Disclaimer

**This project is for research and demonstration purposes only. It is not intended for clinical use or medical decision-making.**

## Project Structure

```text
app/
  ingestion/
  processing/
  retrieval/
  generation/
  pipelines/
  ui/

data/
  raw/
  raw_xml/
  processed/
  vectorstore/

scripts/
  convert_xml.py

tests/
  test_ingestion.py
  test_chunking.py
  test_ingest_pipeline.py
  test_retrieval.py
  test_qa_pipeline.py

 
