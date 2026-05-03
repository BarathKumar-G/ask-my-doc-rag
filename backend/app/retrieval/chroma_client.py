import chromadb
from app.config.settings import CHROMA_PATH


def get_chroma_client():
    return chromadb.PersistentClient(path=CHROMA_PATH)


def get_or_create_collection(client):
    return client.get_or_create_collection(name="rag_collection")