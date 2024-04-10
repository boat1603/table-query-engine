# table-query-engine

## Run with Local

### Step1: Pre-requisites Install

1. Install Python>=3.10.
2. Set `VLLM_ENDPOINT`, `VLLM_API_KEY`, and `MODEL_NAME` to environment.

### Step2: Install Environment

```
$ pip3 install -e .
```

### Step3: Run Local

```
$ python3 -m table_query_engine.server
```

## Run with docker

```
$ docker-compose up -d
```

## DOCS

```
{{BASE_URL}}:8000/docs
```

# API usage

```
$ python3 scripts/api_test.py --query-str "เมืองไหนมีประชากรมากที่สุด" --query-endpoint http://localhost:8000/query
>>> 200 {'response': 'Tokyo'}
```
