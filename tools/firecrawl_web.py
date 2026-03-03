from app.config import FIRECRAWL_API_KEY
import httpx
async def crawl_web_page(url: str) -> str:
    """
    Lightweight async web scraping.
    Used for Wikipedia, blogs, public sites.
    """
    endpoint = "https://api.firecrawl.dev/v1/scrape"

    payload = {
        "url": url,
        "formats": ["text"]
    }

    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}"
    }

    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.post(endpoint, json=payload, headers=headers)
        r.raise_for_status()
        return r.json()["data"]["text"]