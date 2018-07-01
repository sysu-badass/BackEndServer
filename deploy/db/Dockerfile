FROM mysql:5.7.22

ENV LANG C.UTF-8

ADD . /db
WORKDIR /db

COPY ./rbac.sql /docker-entrypoint-initdb.d/rbac.sql

EXPOSE 3306
CMD ["mysqld"]