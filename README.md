# Levenshtein API

A FastAPI-based application for calculating the Levenshtein distance between two strings with caching.

## Prerequisites

- Python 3.11+
- Pipenv (for local setup)
- Docker (for containerized setup)

## Installation and Running Locally

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd <repo_name>
   ```
2. Install dependencies:
   ```sh
   pip install pipenv
   pipenv shell
   pipenv install
   ```
3. Run the FastAPI application:
   ```sh
   pipenv run uvicorn main:app --host 0.0.0.0 --port 8000
   ```
4. Access the API at:
   - OpenAPI Docs: [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)
   - Redoc: [http://0.0.0.0:8000/redoc](http://0.0.0.0:8000/redoc)

## Running with Docker

1. Build the Docker image:
   ```sh
   docker build -t levenshtein-api .
   ```
2. Run the container:
   ```sh
   docker run -p 8000:8000 levenshtein-api
   ```
3. The API will be available at the same endpoints as in the local setup.

## Running Tests

To run tests from `test.py`, use:
```sh
pytest test.py 
```

If running inside Docker:
```sh
docker run --rm levenshtein-api python -m pytest test.py
```

