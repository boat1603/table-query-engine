FROM python:3.11.9
WORKDIR /app
COPY ./pyproject.toml .
COPY ./src ./src
RUN pip install -e .

EXPOSE 8000
CMD ["python", "-m", "table_query_engine.server"]