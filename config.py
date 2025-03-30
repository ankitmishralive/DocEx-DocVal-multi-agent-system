# config.py
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
CHUNK_SIZE = 5000
CHUNK_OVERLAP = 300
PDF_FILE_PATH = "LossRun.pdf"

