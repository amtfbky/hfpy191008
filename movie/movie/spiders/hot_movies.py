# -*- coding:utf-8 -*-

import scrapy
class HotMovies(scrapy.Spider):
	name = "hot_movies"
	start_urls = ["http://www.douban.com/"]
	# 解析数据的方法
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open('./file/'+filname+'.html', 'w') as f:
			f.write(response.body)