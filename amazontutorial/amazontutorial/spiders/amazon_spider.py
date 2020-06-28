# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/Books-Last-30-days/s?rh=n%3A976389031%2Cp_n_publication_date%3A2684819031'
        ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-mini+ .a-spacing-mini .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items