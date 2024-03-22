FROM python:3.12.2-slim

# set work directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY ./config ./config
COPY ./src ./src
