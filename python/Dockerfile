FROM python:3.9

RUN pip install mysql-connector-python
# RUN apt-get update \
#     && apt-get -y install libpq-dev gcc \
#     && pip install psycopg2

WORKDIR /usr/app/src

COPY *.json /python/
#COPY insert_values.py ./
COPY ["docker_output.py", "insert_values.py", "sql_queries.py", "main.py", "./"]

#ENTRYPOINT [ "python3", "insert_values.py", "main.py" ]