# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from re import sub

import scrapy
from scrapy.loader.processors import Compose, MapCompose, TakeFirst
from w3lib.html import remove_tags


def parse_keypair(kp):
    kp = str(kp).lower().split(': ')
    if len(kp) == 2:
        return [kp]


def parse_id(url):
    return str(url).split(': ')[-1]


def strip_price(string):
    return sub(r'[^\d.]', '', string)


class CarLoader(scrapy.loader.ItemLoader):
    default_output_processor = TakeFirst()


class Car(scrapy.Item):
    # define the fields for your item here like:
    attributes = scrapy.Field(
            input_processor=MapCompose(remove_tags, parse_keypair),
            output_processor=Compose(dict)
            )
    contact = scrapy.Field()
    datetime = scrapy.Field()
    id = scrapy.Field(input_processor=MapCompose(parse_id))
    image = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(strip_price))
    url = scrapy.Field()
    vin = scrapy.Field(input_processor=MapCompose(str.upper))
    miles = scrapy.Field()
    spv = scrapy.Field(output_processor=MapCompose(strip_price))
    year = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    title_status = scrapy.Field()
