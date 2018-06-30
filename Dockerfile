FROM python:3.5-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN chmod a+x ./start.sh

EXPOSE 5000

CMD  /bin/sh start.sh
