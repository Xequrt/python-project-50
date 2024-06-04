install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

check: lint test

.PHONY: install test lint check build