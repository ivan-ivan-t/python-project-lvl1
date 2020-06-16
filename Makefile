install:
	@poetry install

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
