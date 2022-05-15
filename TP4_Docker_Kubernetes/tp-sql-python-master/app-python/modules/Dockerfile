FROM mariadb:latest

ADD create_structure.sql /docker-entrypoint-initdb.d/create_structure.sql

ENV MARIADB_ROOT_PASSWORD=password 
ENV MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=password
ENV MARIADB_RANDOM_ROOT_PASSWORD=password

CMD mariadb -u admin -p password create_structure.sql < create-structure.sql
