from firecrawl import FirecrawlApp
from app.config import FIRECRAWL_API_KEY

firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

def fetch_is456_clause(pdf_url: str) -> str:
    """Extract content from single PDF document"""
    try:
        # Simple extract() without params
        result = firecrawl.extract(
            [pdf_url]
        )
        
        print(f"Result type: {type(result)}")  # Debug
        print(f"Result: {result}")  # Debug
        
        # Handle different response formats
        if isinstance(result, list) and len(result) > 0:
            item = result[0]
            if isinstance(item, dict):
                return item.get('text') or item.get('markdown') or item.get('content')
            return str(item)
        elif isinstance(result, dict):
            return result.get('text') or result.get('markdown') or result.get('content')
        else:
            return str(result) if result else None
            
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None