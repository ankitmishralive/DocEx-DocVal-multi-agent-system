

# tools/pdf_loader.py
from typing import List
from langchain_community.document_loaders import PyPDFLoader

def load_and_chunk_pdf(pdf_file_path: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    """Loads a PDF, chunks the content, and returns a list of text chunks."""
    try:
        loader = PyPDFLoader(pdf_file_path)
        documents = loader.load()
        text = "\n".join([doc.page_content for doc in documents])

        # Simple chunking by character count
        chunks = []
        for i in range(0, len(text), chunk_size - chunk_overlap):
            chunk = text[i:i + chunk_size]
            chunks.append(chunk)
        return chunks
    except Exception as e:
        print(f"Error loading/chunking PDF: {str(e)}")
        return []