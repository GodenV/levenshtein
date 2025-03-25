from functools import wraps
from itertools import chain

from cachetools import cached, LRUCache


def make_frozenset_from_args(*args, **kwargs):
    """
    Generates a cache key by converting function arguments into a frozenset.

    This ensures that caching is independent of the argument order,
    making the function cache results consistently.

    Example:
        make_frozenset_from_args(1, 2, a=3, b=4) == make_frozenset_from_args(2, 1, b=4, a=3)

    Returns:
        frozenset: A unique representation of the function arguments.
    """
    return frozenset(chain(args, kwargs.items()))


def unordered_caching(cache: LRUCache):
    """
       A decorator that applies caching to a function, ensuring that results
       are stored based on argument values, regardless of their order.

       Args:
           cache (LRUCache): An instance of `LRUCache` for storing results.
    """
    def decorator(func):
        @cached(cache, key=make_frozenset_from_args)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
