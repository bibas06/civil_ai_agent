import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Civil Engineering AI Assistant",
    layout="wide"
)

st.title("🏗️ Civil Engineering AI Assistant")
st.caption("Dynamic BBS • IS Codes • Real-Time Data")

query = st.text_area(
    "Enter your query:",
    placeholder="Example: Calculate slab BBS for 4x3m slab using 12mm bars @150mm spacing"
)

if st.button("Run Query"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        st.subheader("📤 Response")
        response_box = st.empty()

        try:
            with requests.post(
                BACKEND_URL,
                params={"query": query},
                stream=True,
                timeout=120
            ) as r:
                r.raise_for_status()
                output = ""
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        output += chunk.decode("utf-8")
                        response_box.markdown(output)

        except Exception as e:
            st.error(f"Error: {e}")
