sync:
	pipenv sync
lock:
	pipenv lock
lint:
	pylint main.py
test:
	pipenv run pytest tests
shell:
	pipenv shell
