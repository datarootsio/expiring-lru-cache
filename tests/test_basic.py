"""Basic testing."""

from datetime import datetime
from functools import partial
from time import sleep
from expiring_lru_cache import lru_cache


def call_every_x_secs(func: callable, secs: int) -> list:
    """Run func every x secs."""
    res = []
    for t in range(secs):
        res.append(func())
        sleep(1)
    return res


def test_no_expiration_basic() -> None:
    """Test with no expiration."""
    p = partial(lru_cache()(lambda: datetime.now()))
    res = call_every_x_secs(p, 4)
    assert all([el == res[0] for el in res])


def test_expiration_basic() -> None:
    """Test with expiration."""
    p = partial(lru_cache(expires_after=2)(lambda: datetime.now()))
    res = call_every_x_secs(p, 4)
    assert all([el == res[0] for el in res]) is False
