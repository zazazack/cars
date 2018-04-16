# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from app.items import Car, CarLoader


class CraigslistSpider(CrawlSpider):
    name = 'craigslist'
    allowed_domains = ['houston.craigslist.org']
    start_urls = ['http://houston.craigslist.org/search/cta']

    rules = (
        Rule(LinkExtractor(restrict_css='a.button.next'), follow=True),
        Rule(LinkExtractor(restrict_css='p.result-info',
                           unique=True), callback='parse_item'),
    )

    def parse_item(self, response):
        loader = CarLoader(item=Car(), response=response)
        loader.add_css('attributes', 'p.attrgroup > span')
        loader.add_css('contact', 'a.mailapp::attr(href)')
        loader.add_css('datetime', 'time.date::attr(datetime)')
        loader.add_css('id', 'div.postinginfos > p.postinginfo::text')
        loader.add_css('image', 'img::attr(src)')
        loader.add_css('latitude', 'div#map::attr(data-latitude)')
        loader.add_css('longitude', 'div#map::attr(data-longitude)')
        loader.add_css('name', 'p.attrgroup > span > b::text')
        loader.add_css('price', 'span.price::text')
        loader.add_value('url', response.url)
        return loader.load_item()
