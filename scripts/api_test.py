import argparse
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to test API.")
    parser.add_argument("--query-str", type=str, required=True, help="Query string.")
    parser.add_argument(
        "--query-endpoint",
        type=str,
        default="http://localhost:8000/query",
        help="API endpoints.",
    )
    args = parser.parse_args()

    response = requests.post(args.query_endpoint, json={"query": args.query_str})
    print(response.status_code, response.json())
