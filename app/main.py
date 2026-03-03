from fastapi import FastAPI
from fastapi.responses import StreamingResponse, JSONResponse
from langchain_groq import ChatGroq
from app.graph import build_graph
from app.schemas import QueryRequest
from app.config import GROQ_API_KEY

app = FastAPI()
graph = build_graph()

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0.1,
    streaming=True
)
'''
# ADD THIS: Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Civil AI Agent API",
        "version": "1.0.0",
        "endpoints": {
            "root": "GET /",
            "query": "POST /query",
            "docs": "GET /docs",
            "redoc": "GET /redoc"
        }
    }
'''
# ADD THIS: Health check endpoint
'''@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "civil_ai_agent"}'''

@app.post("/query")
async def query_handler(query: str) -> StreamingResponse:
    async def stream():
        state = await graph.ainvoke({
            "query": query,
            "intent": None,
            "bbs_input": None,
            "bbs_data": None,
            "weather_data": None,
            "material_data": None,
            "iscode_text": None
        })

        prompt = f"""
        Query: {query}
        BBS Data: {state.get("bbs_data")}
        Weather: {state.get("weather_data")}
        Materials: {state.get("material_data")}
        IS Code Text: {state.get("iscode_text")}
        Answer strictly based on above data.
        """

        async for chunk in llm.astream(prompt):
            yield chunk.content

    return StreamingResponse(stream(), media_type="text/plain")