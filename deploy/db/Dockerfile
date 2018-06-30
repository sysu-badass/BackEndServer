FROM mysql:5.7.22

ENV LANG C.UTF-8

ADD . /db
WORKDIR /db

COPY ./rbac.sql /docker-entrypoint-initdb.d/rbac.sql

COPY ./01-my-script.sh /docker-entrypoint-initdb.d/01-my-script.sh
RUN chmod +x /docker-entrypoint-initdb.d/01-my-script.sh

EXPOSE 3306
CMD ["mysqld"]