from typing import List


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)

    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents: List[str]) -> List[str]:
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    return all_chunks