install:
	pip install pipenv
sync:
	pipenv sync
lock:
	pipenv lock
lint:
	pipenv run pylint main.py
test:
	pipenv run pytest tests
shell:
	pipenv shell
build_wheel:
	python setup.py sdist