# expiring_lru_cache

`expiring_lru_cache` is a minimal drop-in replacement of `functools.lru_cache`. It allows the user to specify a time interval (in secs) after which the cache is invalidated and reset.

## Usage

Here an example cached function whose cache will invalidate after 10 seconds.

```python
from expiring_lru_cache import lru_cache

@lru_cache(expires_after=10)
def my_plus_one_func(x: int) -> int:
    return x + 1

```

Here an example cached function whose cache will invalidate after 1 day. Note that the convenience variables `minutes`, `hours` and `days` are available within the `expiring_lru_cache` namespace.

```python
from expiring_lru_cache import lru_cache, days

@lru_cache(expires_after=1 * days)
def my_plus_one_func(x: int) -> int:
    return x + 1

```