lint:
	@flake8 src
	@mypy src
	@black src --check --diff --color

black:
	@black src

test:
	@pytest -ra -q

deps:
	@pip install -Ur requirements-dev.txt

clean:
	@rm -rf env
	@find . -name "__pycache__" -exec rm -rf {} +
	@find . -name "*.egg-info" -exec rm -rf {} +
