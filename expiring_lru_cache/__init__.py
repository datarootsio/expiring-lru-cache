"""Core functionality."""
from datetime import datetime, timedelta
import functools
import logging

logging.getLogger("expiring_lru_cache").addHandler(logging.NullHandler())

minutes = 60
hours = 60 * minutes
days = 24 * hours


def init_cache(
    func: callable, expires_after: int, *args: list, **kwargs: dict
) -> callable:
    """Initialize cached function by wrapping it in functools' lru_cache."""
    cached_func = functools.lru_cache(*args, **kwargs)(func)
    if expires_after:
        setattr(
            cached_func,
            "__expires_at",
            datetime.now() + timedelta(seconds=expires_after),
        )
    return cached_func


def expired(cached_func: callable) -> bool:
    """Check if cached function is expired."""
    if hasattr(cached_func, "__expires_at"):
        return getattr(cached_func, "__expires_at") < datetime.now()
    else:
        return False


def lru_cache(expires_after: int = None, *args: list, **kwargs: dict) -> callable:
    """LRU caching with expiration period.

    Acts as a drop-in replacement of functools.lru_cache. Arguments valid for functools.lru_cache can also be passed to this functions.

    Args:
        expires_after (int, optional): number of seconds after which to invalidate cache. If None, will never invalidate based on time.  The convenience variables `minutes`, `hours` and `days` are provided as to be able to provide e.g. `2 * days` as an invalidation period. Defaults to None.

    Returns:
        callable: cached function
    """

    def decorate(func: callable) -> callable:
        cached_func = init_cache(func, expires_after, *args, **kwargs)

        @functools.wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> callable:
            nonlocal cached_func
            if expired(cached_func):
                logging.debug("resetting cache")
                cached_func = init_cache(func, expires_after, *args, **kwargs)
            return cached_func(*args, **kwargs)

        return wrapper

    return decorate
