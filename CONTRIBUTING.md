# Contributing

Thanks for contributing! Here's some useful information when requesting features/bugfixes.

## Setup

We believe in well linted code. That means we also advocate for linting tools. Amongst
those, we include:

- [`black`](https://black.readthedocs.io/en/stable/)
- [`isort`](https://pycqa.github.io/isort/)
- [`flake8`](https://flake8.pycqa.org/en/latest/) (+[`flake8-docstrings`](https://pypi.org/project/flake8-docstrings/))
- [`mypy`](http://mypy-lang.org/)

(See [`.pre-commit-config.yaml`](https://github.com/datarootsio/expiring-lru-cache/blob/main/.pre-commit-config.yaml) for versions.)

You may notice that these are not included in our
[`pyproject.toml`](https://github.com/datarootsio/expiring-lru-cache/blob/main/pyproject.toml)
😱. How's that, you ask? We use [`pre-commit`](https://pre-commit.com/) to run these
tools, which will create a separate environment for each tool (and avoid some dependency
conflicts!). Though recommended, you don't need to use it, but we'll check that the code
is compliant with these tools. We also package the code and set up environments using
[`poetry`](https://python-poetry.org/). Putting it all together, we have

```console
pip install poetry==1.1.14
git clone git@github.com:datarootsio/expiring-lru-cache.git
cd expiring-lru-cache
poetry install
poetry run pre-commit install
```

## Versioning

We follow [SemVer](https://semver.org/) for package versions. You can check the version
from `expirining_lru_cache.__version__`. This is set dyanamically via CICD and kept in
sync with git tags.

### Git tags

Tagging happens in CICD. See the [CICD file](https://github.com/datarootsio/expiring-lru-cache/blob/main/.github/workflows/publish.yml)
for more information.

## Documentation

Documentation is handled by [`mkdocs`](https://www.mkdocs.org/), and can be created with
markdown files in the `docs/` directory. Documentation is hosted in GitHub pages and is
also deployed via [CICD](https://github.com/datarootsio/expiring-lru-cache/blob/main/.github/workflows/publish.yml).
