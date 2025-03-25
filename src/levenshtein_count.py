from cachetools import LRUCache

from src.cache import unordered_caching


def levenshtein_count(string1: str, string2: str) -> int:

    cache = LRUCache(maxsize=1000) # LRU cache stored within the function (not globally)

    @unordered_caching(cache) # Apply caching to recursive calls
    def levenshtein_count_recursive(s1: str, s2: str):
        if not s1:
            return len(s2)
        if not s2:
            return len(s1)

        if s1[0] == s2[0]:
            return levenshtein_count_recursive(s1[1:], s2[1:])

        replace = 1 + levenshtein_count_recursive(s1[1:], s2[1:])

        insert = 1 + levenshtein_count_recursive(s1, s2[1:])

        delete = 1 + levenshtein_count_recursive(s1[1:], s2)

        return min(replace, insert, delete)

    return levenshtein_count_recursive(string1, string2)
