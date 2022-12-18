FROM python:3.9

RUN pip install mysql-connector-python

WORKDIR /usr/app/src

COPY *.json /python/
COPY insert_values.py ./