# cars

Find a car.

## Prerequistes

- Docker CE

## Install

From source:

    git clone https://github.com/zazazack/cars.git
    cd ./cars
    python -m venv .venv
    python -m pip install -r requirements.txt

<!-- TODO: instructions for docker stack, docker-compose, and/or docker service deploy -->

## Usage

Adhoc run

    scrapy crawl -L INFO --logfile=scrapy.log craigslist

Tail the logs

    tail -f logs/*

View the data

    head ./data/craigslist/*.json
