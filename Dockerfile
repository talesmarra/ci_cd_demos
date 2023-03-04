FROM public.ecr.aws/lambda/python:3.7

WORKDIR /home 

COPY Pipfile.lock .

ENV TRANSFORMERS_CACHE=/tmp

RUN pip install pipenv

RUN pipenv requirements > requirements.txt

COPY main_ml.py ${LAMBDA_TASK_ROOT}

RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "main_ml.lambda_handler" ]
