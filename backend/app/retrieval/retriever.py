from typing import List
from app.retrieval.chroma_client import get_chroma_client, get_or_create_collection


def store_embeddings(chunks: List[str], embeddings: List[List[float]]):
    client = get_chroma_client()
    collection = get_or_create_collection(client)

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    print(f"Stored {len(chunks)} chunks in Chroma")