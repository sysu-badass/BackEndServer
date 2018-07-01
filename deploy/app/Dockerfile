FROM python:3.5-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000

CMD  ["python", "run.py"]
