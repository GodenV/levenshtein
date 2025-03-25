from cachetools import LRUCache
from fastapi import FastAPI

from src.cache import unordered_caching
from src.levenshtein_count import levenshtein_count
from src.schemas import LevenshteinResponse
from settings import config

app = FastAPI(
    title=config.APP_NAME,
    root_path="/api",
)

cache = LRUCache(maxsize=1000)


@app.get("/levenshtein", response_model=LevenshteinResponse)
@unordered_caching(cache)
def get_levenshtein_count(s1: str, s2: str):
    distance = levenshtein_count(s1, s2)
    return LevenshteinResponse(distance=distance)
