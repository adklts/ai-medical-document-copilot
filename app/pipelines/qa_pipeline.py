from app.retrieval.retriever import retrieve_chunks
from app.retrieval.prompt_builder import build_prompt
from app.generation.llm_service import generate_answer

def run_qa_pipeline(query: str, index_path: str, metadata_path: str, top_k: int = 3):
    retrieved_chunks = retrieve_chunks(query, index_path, metadata_path, top_k=top_k)
    prompt = build_prompt(query, retrieved_chunks)
    answer = generate_answer(prompt)

    return {
        "question": query,
        "answer": answer,
        "sources": retrieved_chunks
    }