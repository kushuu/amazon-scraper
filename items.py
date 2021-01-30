# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_img_link = scrapy.Field()
    product_price = scrapy.Field()
    product_stars = scrapy.Field()
    product_ratings = scrapy.Field()