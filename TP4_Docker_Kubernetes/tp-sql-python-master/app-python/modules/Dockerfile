FROM mariadb:latest

ADD create_structure.sql /docker-entrypoint-initdb.d/create_structure.sql

ENV MARIADB_ROOT_PASSWORD=password, MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=password, MARIADB_RANDOM_ROOT_PASSWORD=password
 
