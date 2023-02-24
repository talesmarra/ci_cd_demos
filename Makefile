install:
	pip install pipenv

install-dependencies:
	pipenv install --system

sync:
	pipenv sync
lock:
	pipenv lock
lint:
	pipenv run pylint main.py module/
test:
	pipenv run pytest tests
shell:
	pipenv shell
wheel:
	python setup.py sdist