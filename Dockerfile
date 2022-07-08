FROM python:3.8.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install postgresql-client libpq-dev g++ -y

WORKDIR /angel_store

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .