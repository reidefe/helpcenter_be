FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /helpcenter-be

COPY Pipfile Pipfile.lock /helpcenter-be/
RUN pip install pipenv && pipenv install --system

COPY . /helpcenter-be/