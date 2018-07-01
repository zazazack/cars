FROM python:3

WORKDIR /usr/src
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
  pip install --no-cache-dir -r requirements.txt
COPY ./app .
EXPOSE 6800
CMD ["scrapyd"]
