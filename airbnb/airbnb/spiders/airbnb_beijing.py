# -*- coding: utf-8 -*-
import scrapy
from airbnb.items import AirbnbItem
from scrapy.loader import ItemLoader
import requests 
import json

class AirbnbBeijingSpider(scrapy.Spider):
	name = "airbnb_beijing"
	allowed_domains = ["airbnb.com"]
	address_list = ['北京团结湖','北京王府井','北京劲松','北京复兴门内','北京沙子口','北京草桥','北京大红门','北京五棵松','北京花乡','南锣鼓巷','什刹海','北京西城区德胜门','健德门','广安门','永定门','西直门','东直门','三里屯','朝阳区三元桥','亮马桥','望京','花家地','望京soho','湖光中街','酒仙桥','亮马河','北京朝阳公园','呼家楼','光华路','日坛','崇文门','建国门','北京国贸','北京大望路','北京双井','北京劲松','北京潘家园','东城区天坛','左安门内大街','陶然亭','大栅栏','宣武门','北京金融街','玉渊潭','西城区车公庄','故宫','景山','东城区钟楼','长椿街','甘家口','西城区莲花池','右安门','丰台大观园','广安门外','马连道','玉渊潭','紫竹院','大钟寺','知春路','中关村','五道口','北京市朝阳区大屯路奥林匹克公园（西北门）','西三旗','西二旗','北京上地','圆明园','西单','东单','菜市口','灯市口','东四', '北京大望路', '北京苏州桥','北京紫竹桥','北京清河','广渠门外','北京月坛','北京北太平庄','北京方庄','北京新街口','北京十里铺','北京亮马桥','北京南站','北京右安门','北京牛街','北京六里桥']
	#address_list = ['成都市锦里','成都宽窄巷','春熙路太古里']
	address_dict = {}
	headers = {
    	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.3 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.3',
    	'From': 'airbnb.com'  # This is another valid field
	}
	for i in address_list:
		r = requests.get('https://zh.airbnb.com/search/search_results?location={}&page=1'.format(i),headers = headers)
		try:
			address_dict[i] = r.json()['logging_info']['search']['result']['totalHits'] / 18 + 1
			print r.json()['logging_info']['search']['result']['totalHits']
		except KeyError,e:
			continue
		except ValueError,e:
			continue
		print i,address_dict[i]
	start_urls = []
	for i in address_dict:
		for j in range(1,address_dict[i] + 1):
			start_urls.append("https://zh.airbnb.com/search/search_results?location={}&page={}".format(i,j))

	def parse(self, response):
		#l = ItemLoader(item = ItjuziItem(),response=response)
		jsonresponse = json.loads(response.body_as_unicode())
		for i in range(0,len(jsonresponse['results_json']['search_results'])):
			l = ItemLoader(item = AirbnbItem(),response=response)
			bedrooms         = jsonresponse['results_json']['search_results'][i]['listing']['bedrooms']
			beds             = jsonresponse['results_json']['search_results'][i]['listing']['beds']
			name             = jsonresponse['results_json']['search_results'][i]['listing']['name']
			person_capacity  = jsonresponse['results_json']['search_results'][i]['listing']['person_capacity']
			primary_host     = jsonresponse['results_json']['search_results'][i]['listing']['primary_host']['first_name']
			host_id          = jsonresponse['results_json']['search_results'][i]['listing']['primary_host']['id']
			host_url         = "https://zh.airbnb.com/users/show/{}".format(host_id)
			property_type    = jsonresponse['results_json']['search_results'][i]['listing']['property_type']
			room_id          = jsonresponse['results_json']['search_results'][i]['listing']['id']
			room_url         = "https://zh.airbnb.com/rooms/{}".format(room_id)
			is_new_listing   = jsonresponse['results_json']['search_results'][i]['listing']['is_new_listing']
			public_address   = jsonresponse['results_json']['search_results'][i]['listing']['public_address']
			room_type        = jsonresponse['results_json']['search_results'][i]['listing']['room_type']
			star_rating      = jsonresponse['results_json']['search_results'][i]['listing']['star_rating']
			reviews_count    = jsonresponse['results_json']['search_results'][i]['listing']['reviews_count']
			guests           = jsonresponse['results_json']['search_results'][i]['pricing_quote']['guests']
			amount           = jsonresponse['results_json']['search_results'][i]['pricing_quote']['rate']['amount']
			currency         = jsonresponse['results_json']['search_results'][i]['pricing_quote']['rate']['currency']
			l.add_value('bedrooms',bedrooms)
			l.add_value('beds',beds)
			l.add_value('name',name)
			l.add_value('person_capacity',person_capacity)
			l.add_value('primary_host',primary_host)
			l.add_value('host_id',host_id)
			l.add_value('host_url',host_url)
			l.add_value('property_type',property_type)
			l.add_value('room_id',room_id)
			l.add_value('room_url',room_url)
			l.add_value('is_new_listing',is_new_listing)
			l.add_value('public_address',public_address)
			l.add_value('room_type',room_type)
			l.add_value('star_rating',star_rating)
			l.add_value('reviews_count',reviews_count)
			l.add_value('guests',guests)
			l.add_value('amount',amount)
			l.add_value('currency',currency)
			print l
			yield l.load_item()
