FROM centos:latest AS base
ENV PYTHONUNBUFFERED=1
RUN yum update -y && yum install -y python3
RUN adduser scrapy
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt && rm -rf requirements.txt
COPY ./app/ ./app/
