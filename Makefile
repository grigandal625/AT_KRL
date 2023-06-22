help:
	@echo "Tasks in \033[1;32mdemo\033[0m:"
	@cat Makefile

lint:
	mypy src --ignore-missing-imports
	flake8 src --ignore=$(shell cat .flakeignore)

dev:
	pipenv run python setup.py develop

test: dev
	pytest


clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/