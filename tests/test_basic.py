"""Basic testing."""

from datetime import datetime, timedelta
from functools import partial
from time import sleep
from typing import Callable

from expiring_lru_cache import lru_cache


def call_every_x_secs(func: Callable, secs: int) -> list:
    """Run func every x secs."""
    res = []
    for _ in range(secs):
        res.append(func())
        sleep(1)
    return res


def test_no_expiration_basic() -> None:
    """Test with no expiration."""
    p = partial(lru_cache()(lambda: datetime.now()))
    res = call_every_x_secs(p, 4)
    assert all(el == res[0] for el in res)


def test_expiration_basic() -> None:
    """Test with expiration."""
    p = partial(lru_cache(expires_after=2)(lambda: datetime.now()))
    res = call_every_x_secs(p, 4)
    assert any(el != res[0] for el in res)


def test_expiration_with_func_args() -> None:
    """Test with expiration."""

    @lru_cache(expires_after=2)
    def get_time(secs: int):
        # get current time and add secs
        curr_time = datetime.now()
        return curr_time + timedelta(seconds=secs)

    p = partial(get_time, 2)
    res = call_every_x_secs(p, 4)
    assert any(el != res[0] for el in res)


def test_expiration_with_func_args_as_partial() -> None:
    """Test with expiration."""

    def get_time(secs: int):
        # get current time and add secs
        curr_time = datetime.now()
        return curr_time + timedelta(seconds=secs)

    p = partial(lru_cache(expires_after=2), partial(get_time, 2))
    res = call_every_x_secs(p, 4)
    assert any(el != res[0] for el in res)


def test_has_cache_info() -> None:
    """Test if cache has info."""
    cf = lru_cache()(lambda: 1)
    for _ in range(3):
        cf()
    assert cf.cache_info().hits != 0
