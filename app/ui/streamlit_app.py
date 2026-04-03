import os
import streamlit as st

from app.pipelines.ingest_pipeline import run_ingest_pipeline
from app.pipelines.qa_pipeline import run_qa_pipeline

INDEX_PATH = "data/vectorstore/faiss_index.bin"
METADATA_PATH = "data/vectorstore/metadata.pkl"
RAW_DATA_DIR = "data/raw"

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs("data/vectorstore", exist_ok=True)

st.set_page_config(
    page_title="AI Medical Document Copilot",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
    /* Background */
    .stApp {
        background-color: #f4f7f7;
    }

    /* Main container */
    .main {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Titles */
    h1 {
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #1f3a3d;  /* petrol dark */
    }

    h2, h3 {
        font-size: 1.6rem !important;
        color: #2f4f4f;
    }

    /* Subtitle */
    .subtitle {
        font-size: 1.3rem;
        color: #5f7a7a;
        margin-bottom: 2rem;
    }

    /* Section titles */
    .section-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f3a3d;
        margin-top: 1.5rem;
        margin-bottom: 0.7rem;
    }

    /* Answer box */
    .answer-box {
        background: #ffffff;
        border-left: 6px solid #2c7be5;
        border-radius: 12px;
        padding: 1.5rem;
        font-size: 1.25rem;
        line-height: 1.8;
        color: #243447;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);  /* thin shadow */
        margin-bottom: 1.2rem;
    }

    /* Info box */
    .info-box {
        background: #ffffff;
        border-radius: 12px;
        padding: 1rem;
        font-size: 1.15rem;
        color: #334155;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        margin-bottom: 1.2rem;
    }

    /* Inputs */
    .stTextInput input {
        font-size: 1.1rem !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        background-color: #2f4f4f;
        color: white;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .stButton > button:hover {
        background-color: #3f6f6f;
    }

    /* Evidence text */
    .evidence-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #243447;
    }

    /* Expanders */
    .streamlit-expanderHeader {
        font-size: 1.1rem !important;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🧠 AI Medical Document Copilot")
st.markdown(
    '<div class="subtitle">Clinical document analysis with Retrieval-Augmented Generation (RAG) and a local LLM</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="info-box"><b>Purpose:</b> Upload a medical document, process it into searchable chunks, and ask grounded questions with evidence-backed answers.</div>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Upload a medical document",
    type=["txt", "pdf"]
)

if "document_processed" not in st.session_state:
    st.session_state.document_processed = False

if "current_file_name" not in st.session_state:
    st.session_state.current_file_name = None

if uploaded_file is not None:
    save_path = os.path.join(RAW_DATA_DIR, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns([1, 4])

    with col1:
        process_clicked = st.button("Process document", use_container_width=True)

    with col2:
        st.caption(f"Selected file: **{uploaded_file.name}**")

    if process_clicked:
        with st.spinner("Processing document..."):
            result = run_ingest_pipeline(
                file_path=save_path,
                index_path=INDEX_PATH,
                metadata_path=METADATA_PATH
            )

        st.session_state.document_processed = True
        st.session_state.current_file_name = uploaded_file.name

        st.success(
            f"Document processed successfully. Total chunks created: {result['num_chunks']}"
        )

question = st.text_input(
    "🔎 Ask a clinical question",
    placeholder="Example: What medications are mentioned in the document?"
)

get_answer_clicked = st.button("Get answer")

if get_answer_clicked:
    if not st.session_state.document_processed:
        st.warning("Please process a document before asking a question.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            result = run_qa_pipeline(
                query=question,
                index_path=INDEX_PATH,
                metadata_path=METADATA_PATH,
                top_k=3
            )

        st.markdown('<div class="section-title">🧠 Answer</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="answer-box">{result["answer"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">📚 Evidence</div>', unsafe_allow_html=True)

        for source in result["sources"]:
            with st.expander(f"Chunk {source['chunk_id']}"):
                st.markdown(
                    f'<div class="evidence-text">{source["text"]}</div>',
                    unsafe_allow_html=True
                )