import os
import argparse
import uvicorn
import pandas as pd

from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from .models import QueryInput, QueryResponse

from llama_index.llms.openai_like import OpenAILike
from llama_index.core.query_engine import PandasQueryEngine

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = OpenAILike(
    model=os.environ["MODEL_NAME"],
    api_key=os.environ["VLLM_API_KEY"],
    api_base=os.environ["VLLM_ENDPOINT"],
)
df = pd.DataFrame(
    {
        "city": ["Toronto", "Tokyo", "Berlin"],
        "population": [2930000, 13960000, 3645000],
    }
)
query_engine = PandasQueryEngine(df=df, llm=llm, verbose=True)


@app.get("/ping")
def ping():
    return {"status": "OK"}


@app.post("/query")
async def query(data: QueryInput) -> QueryResponse:
    response = query_engine.query(data.query)
    return QueryResponse(response=response.response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Table query engine.")
    parser.add_argument("--port", type=int, default="8000", help="Server port number.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address.")
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
