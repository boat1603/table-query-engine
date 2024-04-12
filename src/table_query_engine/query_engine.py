import os
import pandas as pd
from .models import QueryResponse

from llama_index.llms.openai_like import OpenAILike
from llama_index.core.query_engine import PandasQueryEngine


class QueryEngine:
    def __init__(self, llm, df):
        self.query_engine = PandasQueryEngine(df=df, llm=llm, verbose=True)

    def __call__(self, query_str) -> QueryResponse:
        response = self.query_engine.query(query_str)
        return QueryResponse(response=response.response)


def initialize_query_engine():
    # VLLM OpenAILike API
    llm = OpenAILike(
        model=os.environ["MODEL_NAME"],
        api_key=os.environ["VLLM_API_KEY"],
        api_base=os.environ["VLLM_ENDPOINT"],
    )
    # Or you can use VLLM directly from this docs: https://docs.llamaindex.ai/en/stable/examples/llm/vllm/
    # Or you can select another llm from `llama_index`.
    df = pd.DataFrame(
        {
            "city": ["Toronto", "Tokyo", "Berlin"],
            "population": [2930000, 13960000, 3645000],
        }
    )
    return QueryEngine(llm, df)
