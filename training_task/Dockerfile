FROM python:3.9.17-slim

ENV APP_DIR /ml-pipeline

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

COPY . .
RUN apt-get update
RUN apt-get install libgomp1
RUN pip install -r requirements.txt
ENV MODEL_S3_BUCKET_NAME=terraform-20230901195624999800000002
ENV DATA_S3_BUCKET_NAME=terraform-20230901195624999400000001
CMD ["python", "main.py"]