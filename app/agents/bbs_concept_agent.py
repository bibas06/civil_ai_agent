from app.tools.firecrawl_pdf import fetch_is456_clause

async def bbs_concept_agent(state):
    state["bbs_data"] = {
        "definition": "Bar Bending Schedule (BBS)",
        "source": "IS 2502 / IS 456",
        "raw_is_code_text":  fetch_is456_clause("https://law.resource.org/pub/in/bis/S03/is.456.2000.pdf")
    }
    return state
