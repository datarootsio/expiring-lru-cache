"""Core functionality."""
import functools
import logging
from datetime import datetime, timedelta
from typing import Any, Callable, Optional, Union

from expiring_lru_cache.version import __version__  # noqa: F401

logging.getLogger("expiring_lru_cache").addHandler(logging.NullHandler())

MINUTES = 60
HOURS = 60 * MINUTES
DAYS = 24 * HOURS


# Bug in type hints for `functools.lru_cache` + mypy
# https://github.com/python/mypy/issues/5858#issuecomment-932773127
def _init_cache(
    func: Callable, expires_after: Optional[int], *args: Any, **kwargs: Any
) -> Callable:
    """Initialize cached function by wrapping it in `functools.lru_cache`."""
    cached_func = functools.lru_cache(*args, **kwargs)(func)
    if expires_after:
        setattr(
            cached_func,
            "__expires_at",
            datetime.now() + timedelta(seconds=expires_after),
        )
    return cached_func


def _expired(cached_func: Callable) -> bool:
    """Check if cached function is expired."""
    if hasattr(cached_func, "__expires_at"):
        return getattr(cached_func, "__expires_at") < datetime.now()
    return False


def lru_cache(
    expires_after: Optional[int] = None,
    *args: Union[int, bool],
    **kwargs: Union[int, bool]
) -> Callable:
    """
    LRU caching with expiration period.

    Acts as a drop-in replacement of `functools.lru_cache`. Arguments valid for
     `functools.lru_cache` can also be passed.
    :param expires_after: number of seconds after which to invalidate cache - `None`
     will never invalidate based on time. Convenience variables `MINUTES`, `HOURS`
     and `DAYS` are available (using `lru_cache(expires_after=2 * DAYS)`)
    :param args: `functools.lru_cache`'s positional arguments
    :param kwargs: `functools.lru_cache`'s keyword arguments
    :return: cached function
    """

    def decorate(func: Callable) -> Callable:
        cached_func = _init_cache(func, expires_after, *args, **kwargs)

        @functools.wraps(func)
        def wrapper(*args: Union[int, bool], **kwargs: Union[int, bool]) -> Callable:
            nonlocal cached_func
            if _expired(cached_func):
                logging.debug("Resetting cache")
                cached_func = _init_cache(func, expires_after, *args, **kwargs)
            return cached_func(*args, **kwargs)

        wrapper.cache_info = lambda: cached_func.cache_info()
        return wrapper

    return decorate
