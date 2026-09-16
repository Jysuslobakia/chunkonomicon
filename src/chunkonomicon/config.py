import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    textbook_pdf_path: str = os.getenv("TEXTBOOK_PDF_PATH", "data/sample/sample_lesson.md")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-004")
    llm_model: str = os.getenv("LLM_MODEL", "gemini-1.5-pro")
    vectorstore_backend: str = os.getenv("VECTORSTORE_BACKEND", "faiss")
    vectorstore_path: str = os.getenv("VECTORSTORE_PATH", "data/processed/index")

settings = Settings()
