install:
	@poetry install

lint:
	poetry run flake8 brain_games

test:
	poetry run pytest brain_games tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
