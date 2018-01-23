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
            Rule(LinkExtractor(restrict_css='p.result-info', unique=True), callback='parse_item'),
    )

    def parse_item(self, response):
        l = CarLoader(item=Car(), response=response)
        l.add_css('attributes', 'p.attrgroup > span')
        l.add_css('contact', 'a.mailapp::attr(href)')
        l.add_css('datetime', 'time.date::attr(datetime)')
        l.add_css('id', 'div.postinginfos > p.postinginfo::text')
        l.add_css('image', 'img::attr(src)')
        l.add_css('latitude', 'div#map::attr(data-latitude)')
        l.add_css('longitude', 'div#map::attr(data-longitude)')
        l.add_css('name', 'p.attrgroup > span > b::text')
        l.add_css('price', 'span.price::text')
        l.add_value('url', response.url)
        return l.load_item()
