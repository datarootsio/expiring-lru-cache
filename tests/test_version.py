"""Test versioning mechanism."""

import expiring_lru_cache


def test_get_version() -> None:
    """Get the current package version."""
    local_version = expiring_lru_cache.__version__
    assert local_version == "0.0.0-dev"  # dynamically set in CI
