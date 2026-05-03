from sentence_transformers import SentenceTransformer
from typing import List


# Load model once (important)
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: List[str]) -> List[List[float]]:
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings.tolist()