import streamlit as st
from app.pipelines.ingest_pipeline import run_ingest_pipeline
from app.pipelines.qa_pipeline import run_qa_pipeline

INDEX_PATH = "data/vectorstore/faiss_index.bin"
METADATA_PATH = "data/vectorstore/metadata.pkl"

st.title("AI Medical Document Copilot")

uploaded_file = st.file_uploader("Upload a medical document", type=["pdf", "txt"])

if uploaded_file is not None:
    save_path = f"data/raw/{uploaded_file.name}"
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process document"):
        result = run_ingest_pipeline(save_path, INDEX_PATH, METADATA_PATH)
        st.success(f"Document processed. Total chunks: {result['num_chunks']}")

question = st.text_input("Ask a question about the document")

if st.button("Get answer"):
    result = run_qa_pipeline(question, INDEX_PATH, METADATA_PATH)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Evidence")
    for source in result["sources"]:
        with st.expander(f"Chunk {source['chunk_id']}"):
            st.write(source["text"])