# -*- coding: utf-8 -*-
from airbnb.items import AirbnbCalItem
from scrapy.selector import Selector
import scrapy
import pandas as pd
import json

class AirbnbBeijingCalSpider(scrapy.Spider):
	name = "airbnb_beijing_cal"
	allowed_domains = ["airbnb.com"]
	start_urls = []
	df = pd.read_csv('./airbnb_beijing.11.13.csv')
	for i in df['room_id']:
		start_urls.append("https://www.airbnb.com/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=cny&locale=zh-cn&listing_id={}&month=9&year=2016&count=3&_format=with_conditions".format(i))
	#start_urls.append("https://www.airbnb.com/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=cny&locale=zh-cn&listing_id=9719293&month=9&year=2016&count=3&_format=with_conditions")
	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		item = AirbnbCalItem()
		item['room_id'] = response.url[120:-51]
		item['min_nights'] = jsonresponse['calendar_months'][0]['condition_ranges'][0]['conditions']['min_nights']
		for i in range(0,3):
			for day in jsonresponse['calendar_months'][i]['days']:
				item['{}'.format(day['date'])] = day['available']
		return item

