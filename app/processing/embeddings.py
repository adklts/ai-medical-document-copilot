from sentence_transformers import SentenceTransformer
from app.core.config import EMBEDDING_MODEL

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model

def embed_texts(texts):
    model = get_embedding_model()
    return model.encode(texts, convert_to_numpy=True)

def embed_query(query: str):
    model = get_embedding_model()
    return model.encode([query], convert_to_numpy=True)[0]