FROM python:3.9.17-slim

ENV APP_DIR /ml-pipeline

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY . .
RUN apt-get update
RUN apt-get install libgomp1
CMD ["python", "main.py"]