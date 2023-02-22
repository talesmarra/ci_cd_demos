FROM python:3.7-alpine

WORKDIR /home 

COPY ./Pipfile Pipfile.lock main.py ./

COPY ./module/ module/

RUN pip install pipenv

RUN pipenv install --system

ENTRYPOINT [ "python", "main.py"]
