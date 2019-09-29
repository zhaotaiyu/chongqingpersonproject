# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PersonInformationItem(scrapy.Item):
	collection = "personinformation"
	person_id = scrapy.Field()
	person_name = scrapy.Field()
	province_person_id = scrapy.Field()
	company_name = scrapy.Field()
	province_company_id = scrapy.Field()
	person_sex = scrapy.Field()
	nation = scrapy.Field()
	birthday = scrapy.Field()
	in_date = scrapy.Field()
	year = scrapy.Field()
	tel = scrapy.Field()
	phone = scrapy.Field()
	url = scrapy.Field()
	department = scrapy.Field()
	person_identification_type = scrapy.Field()
	person_identification_id = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()
	company_id = scrapy.Field()
class PersonCertificateItem(scrapy.Item):
	collection = "personcertificate"
	person_id = scrapy.Field()
	province_person_id = scrapy.Field()
	aptitude_name = scrapy.Field()
	certificate_num = scrapy.Field()
	reg_num = scrapy.Field()
	reg_credential_num = scrapy.Field()
	certificate_useful_time = scrapy.Field()
	aptitude_accept_date = scrapy.Field()
	title = scrapy.Field()
	duty = scrapy.Field()
	worklicense_num = scrapy.Field()
	major = scrapy.Field()
	level = scrapy.Field()
	aptitude_type = scrapy.Field()
	certificate_seal_id = scrapy.Field()
	company_name = scrapy.Field()
	certificate_company_name = scrapy.Field()
	certificate_company_id = scrapy.Field()
	create_time = scrapy.Field()
	modification_time = scrapy.Field()
	is_delete = scrapy.Field()
	source = scrapy.Field()
	status = scrapy.Field()
	person_name = scrapy.Field()

