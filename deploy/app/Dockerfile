FROM python:3.5-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD  ["python", "run.py"]
