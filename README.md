<p align="center">
  <a href="https://datarootsio.github.io/expiring-lru-cache/"><img alt="logo" src="https://raw.githubusercontent.com/datarootsio/expiring-lru-cache/main/docs/images/dall_e_logo.png" height="200"></a>
</p>

# `expiring_lru_cache`
<p align="left">
  <a href="https://dataroots.io"><img alt="Maintained by dataroots" src="https://dataroots.io/maintained-rnd.svg" /></a>
  <a href="https://pypi.org/project/expiring-lru-cache/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/expiring-lru-cache" /></a>
  <a href="https://pypi.org/project/expiring-lru-cache/"><img alt="PiPy" src="https://img.shields.io/pypi/v/expiring-lru-cache" /></a>
  <a href="https://pepy.tech/project/expiring-lru-cache"><img alt="Downloads" src="https://pepy.tech/badge/expiring-lru-cache" /></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>
  <a href="http://mypy-lang.org/"><img alt="Mypy checked" src="https://img.shields.io/badge/mypy-checked-1f5082.svg" /></a>
  <a href="https://app.codecov.io/gh/datarootsio/expiring-lru-cache"><img alt="Codecov" src="https://codecov.io/github/datarootsio/expiring-lru-cache/main/graph/badge.svg" /></a>
  <a href="https://github.com/datarootsio/expiring-lru-cache/actions"><img alt="test" src="https://github.com/datarootsio/expiring-lru-cache/actions/workflows/tests.yml/badge.svg" /></a>
</p>

`expiring_lru_cache` is a minimal drop-in replacement of `functools.lru_cache`. It
allows the user to specify a time interval (in secs) after which the cache is
invalidated and reset.

## Usage

Here an example cached function whose cache will invalidate after 10 seconds.

```python
from expiring_lru_cache import lru_cache

@lru_cache(expires_after=10)
def my_plus_one_func(x: int) -> int:
    return x + 1
```

Here an example cached function whose cache will invalidate after 1 day. Note that the
convenience variables `MINUTES`, `HOURS` and `DAYS` are available within the
`expiring_lru_cache` namespace.

```python
from expiring_lru_cache import lru_cache, DAYS


@lru_cache(expires_after=1 * DAYS)
def my_plus_one_func(x: int) -> int:
    return x + 1
```
