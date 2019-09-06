# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PersonInformationItem(scrapy.Item):
	collection = "personinformation"
	name = scrapy.Field()
	major = scrapy.Field()
	title_level = scrapy.Field()
	person_type = scrapy.Field()
	company_name = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	mark = scrapy.Field()
	person_genre = scrapy.Field()
	credential_num = scrapy.Field()
	sex = scrapy.Field()
	seal_num = scrapy.Field()
	reg_num = scrapy.Field()
	reg_credential_num = scrapy.Field()
	aptitude_useful_date = scrapy.Field()
	aptitude_speciality = scrapy.Field()
	aptitude_accept_date = scrapy.Field()
	nation = scrapy.Field()
	birthday = scrapy.Field()
	title = scrapy.Field()
	duty = scrapy.Field()
	worklicense_num = scrapy.Field()
	in_date = scrapy.Field()
	year = scrapy.Field()
	tel = scrapy.Field()
	phone = scrapy.Field()
	major2 = scrapy.Field()
	admissionticket_num = scrapy.Field()
	handle_type = scrapy.Field()
	department = scrapy.Field()
	status = scrapy.Field()

