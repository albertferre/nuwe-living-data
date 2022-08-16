FROM python:3.9.13-alpine3.16


WORKDIR /app

copy requirements.txt requirements.txt
COPY src/* src/
copy .env .env
COPY crontab crontab
COPY main.py main.py

RUN pip install -r requirements.txt
RUN crontab crontab

CMD ["crond", "-f"]