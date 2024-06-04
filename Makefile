install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

lint:
	poetry run flake8 gendiff

check: lint test

.PHONY: install test lint check build