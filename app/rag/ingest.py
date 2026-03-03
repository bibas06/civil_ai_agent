from app.tools.firecrawl_pdf import fetch_is456_clause
from langchain_text_splitters import RecursiveCharacterTextSplitter

IS456_PDF = "https://svvv.edu.in/assets/pdf/Institute/Civil%20Engineering/IS%20456-2000.pdf"

def ingest_is456():
    raw_text = fetch_is456_clause(IS456_PDF)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    return splitter.split_text(raw_text)
