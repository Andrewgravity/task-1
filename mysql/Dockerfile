FROM mysql:latest

# copy the sql file and run it
COPY ["./rooms.sql", "./students.sql"] /docker-entrypoint-initdb.d/
# COPY ./students.sql /docker-entrypoint-initdb.d/
