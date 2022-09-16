FROM python:3.7

WORKDIR /home

COPY ./Pipfile Pipfile

COPY ./Pipfile.lock Pipfile.lock

COPY ./main.py main.py

RUN pip install pipenv

RUN pipenv run pip freeze > requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
