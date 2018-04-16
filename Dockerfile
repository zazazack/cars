FROM python:3 as scrapy

WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
  pip install -r requirements.txt
COPY ./app ./app
EXPOSE 6800
CMD ["scrapyd"]
