import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Default fallback if env not set
CHROMA_PATH = os.getenv("CHROMA_PATH", "vector_store/chroma_db")