import argparse
import uvicorn

from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware
from .models import QueryInput, QueryResponse
from .query_engine import initialize_query_engine


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

query_engine = initialize_query_engine()


@app.get("/ping")
def ping():
    return {"status": "OK"}


@app.post("/query")
async def query(data: QueryInput) -> QueryResponse:
    response = query_engine(data.query)
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Table query engine.")
    parser.add_argument("--port", type=int, default="8000", help="Server port number.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address.")
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
