import argparse
import json
import time

############################
# You can edit you code HERE
from table_query_engine import initialize_query_engine

############################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to execute query engine.")
    parser.add_argument(
        "--query-json", type=str, required=True, help="Path to json of quert str."
    )
    parser.add_argument(
        "--save-dir",
        type=str,
        default="./output.jsonl",
        help="Path to output response.",
    )
    args = parser.parse_args()

    ############################
    # You can edit you code HERE
    query_engine = initialize_query_engine()
    ############################

    with open(args.query_json, "r") as f:
        query_json = json.load(f)
    # Reset save_dir
    with open(args.save_dir, "w") as f:
        pass

    for query_str in query_json:
        t1 = time.time()
        response = query_engine(query_str).response
        elapsed_time = time.time() - t1
        with open(args.save_dir, "a") as f:
            json.dump({"response": response, "elapsed_time": elapsed_time}, f)
            f.write("\n")
