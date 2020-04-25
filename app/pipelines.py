# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from mechanicalsoup import StatefulBrowser
from scrapy.exceptions import DropItem

from app.items import strip_price

class AppPipeline(object):
    def process_item(self, item, spider):
        if item['attributes']:
            if item['attributes'].get('vin') and item['attributes'].get('odometer'):
                item['vin'] = item['attributes'].pop('vin')
                item['miles'] = item['attributes'].pop('odometer')

                spv = dict(self.get_spv(vin=item['vin'],
                                        miles=item['miles']))
                item['spv'] = strip_price(spv.get('Private Value'))
                item['year'], item['make'], item['model'] = spv.get('Vehicle').split()[:3]
            else:
                raise DropItem('Missing value')

        return item

    def get_spv(self, vin, miles, *args, **kwargs):
        """Get the Standard Presumptive Value (SPV)."""
        browser = StatefulBrowser()
        browser.open('https://tools.txdmv.gov/tools/std_presumptive_value/')
        browser.select_form('form[name="VehicleInfo"]')
        browser['vin'] = vin
        browser['miles'] = int(miles)
        browser.submit_selected()
        for tr in browser.get_current_page().select('table#result > tr'):
            split = tr.text.strip().split(': ')
            if len(split) == 2:
                yield split
