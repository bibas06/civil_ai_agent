from app.tools.firecrawl_pdf import fetch_is456_clause

async def code_agent(state):
    state["iscode_text"] = fetch_is456_clause("https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf")
    return state
