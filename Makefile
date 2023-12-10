# sudo docker run -it --rm -v $$(pwd)/src/at_krl/grammar:/app qmu1/antlr4:latest sh -c "cd /app && java -jar /antlr4.jar -Dlanguage=Python3 test.g4" 
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
antlr:
	sudo docker run -it --rm -v $$(pwd)/src/at_krl/grammar:/app antlr/antlr4 -Dlanguage=Python3 /app/at_krl.g4
    
build: clean
	pip install wheel
	python setup.py bdist_wheel
stable:
	cp dist/at_krl-*.*-py3-none-any.whl dist/at_krl-stable-py3-none-any.whl
latest:
	cp dist/at_krl-*.*-py3-none-any.whl dist/at_krl-latest-py3-none-any.whl