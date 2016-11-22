# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy


class AirbnbItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	bedrooms = scrapy.Field()
	beds = scrapy.Field()
	name  = scrapy.Field()
	person_capacity  = scrapy.Field()
	primary_host  = scrapy.Field()
	host_id  = scrapy.Field()
	host_url  = scrapy.Field()
	property_type  = scrapy.Field()
	room_id = scrapy.Field()
	room_url  = scrapy.Field()
	is_new_listing  = scrapy.Field()
	public_address  = scrapy.Field()
	room_type  = scrapy.Field()
	star_rating  = scrapy.Field()
	reviews_count  = scrapy.Field()
	guests  = scrapy.Field()
	amount  = scrapy.Field()
	currency  = scrapy.Field()
	lat       = scrapy.Field()
	lng       = scrapy.Field()

class AirbnbCalItem(Item):
	def __setitem__(self, key, value):
		if key not in self.fields:
			self.fields[key] = Field()
		self._values[key] = value