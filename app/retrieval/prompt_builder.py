def build_prompt(query: str, retrieved_chunks: list) -> str:
    context = "\n\n".join(
        [f"Chunk {chunk['chunk_id']}:\n{chunk['text']}" for chunk in retrieved_chunks]
    )

    prompt = f"""
You are a medical document assistant.
Answer the question only using the context below.
If the answer is not present in the context, say: "The answer is not available in the document."
Be concise and grounded.

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt.strip()