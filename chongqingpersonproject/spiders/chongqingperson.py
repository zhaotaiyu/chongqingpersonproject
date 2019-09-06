# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json,datetime
from lxml import etree
from chongqingpersonproject.items import *

class ChongqingpersonSpider(scrapy.Spider):
	name = 'chongqingperson'
	allowed_domains = ['183.66.171.75:88']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx']
	#start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx']
	start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx']

	def parse(self, response):
		total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
		if total_page is None:
			total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
		print(total_page)
		# for num in range(1,int(total_page)+1):
		for num in range(8,12):
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx":
				yield Request(response.url,callback=self.parse_zcjzs,meta={"num":num,"mark":"zcjzs","line":1,"page":"Pager1_NewPage","go":"Pager1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx":
				yield Request(response.url,callback=self.parse_zczjs,meta={"num":num,"mark":"zczjs","line":2,"page":"Pager1_NewPage","go":"Pager1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx":
				yield Request(response.url,callback=self.parse_zljcry,meta={"num":num,"mark":"zljcry","line":2,"page":"Pager1_NewPage","go":"Pager1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx":
				yield Request(response.url,callback=self.parse_cqsjly,meta={"num":num,"mark":"cqsjly","page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx":
				yield Request(response.url,callback=self.parse_cqsjlgcs,meta={"num":num,"mark":"cqsjlgcs","page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx":
				yield Request(response.url,callback=self.parse_zcjlgcs,meta={"num":num,"mark":"zcjlgcs","page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx":
				yield Request(response.url,callback=self.parse_zzaqry,meta={"num":num,"mark":"zzaqry","line":2,"page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx":
				yield Request(response.url,callback=self.parse_xmaqfzr,meta={"num":num,"mark":"xmaqfzr","line":2,"page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx":
				yield Request(response.url,callback=self.parse_qyaqfzr,meta={"num":num,"mark":"qyaqfzr","line":2,"page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx":
				yield Request(response.url,callback=self.parse_tzzyry,meta={"num":num,"mark":"tzzyry","page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)
			if response.url =="http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx":
				yield Request(response.url,callback=self.parse_zbdlzzry,meta={"num":num,"mark":"zbdlzzry","line":2,"page":"TurnPage1_PageNum","go":"TurnPage1_BT_Go"},dont_filter=True)


	# 注册建造师
	def parse_zcjzs(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='_FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='_FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='_FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:
				p_info["reg_num"] = response.xpath("//span[@id='_FNumber']/text()")[0]
			except:
				p_info["reg_num"] = None
			try:
				p_info["seal_num"] = response.xpath("//span[@id='_FVerifyNumber']/text()")[0]
			except:
				p_info["seal_num"] = None
			try:
				p_info["reg_credential_num"] = response.xpath("//span[@id='_FQNumber']/text()")[0]
			except:
				p_info["reg_credential_num"] = None
			try:
				p_info["aptitude_useful_date"] = response.xpath("//span[@id='_FValidDate']/text()")[0]
			except:
				p_info["aptitude_useful_date"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			# try:
			tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
			if len(tr_list):
				for tr in tr_list[1:]:
					try:
						p_info["credential_num"] = tr.xpath("./td[2]/text()")[0]
					except:
						p_info["credential_num"] = None
					try:
						p_info["aptitude_speciality"] = tr.xpath("./td[1]/text()")[0]
					except:
						p_info["aptitude_speciality"] = None
					try:
						p_info["aptitude_accept_date"] = tr.xpath("./td[3]/text()")[0]
					except:
						p_info["aptitude_accept_date"] = None
					yield p_info
			else:
				try:
					p_info["sex"] = response.xpath("//span[@id='_FSex']/font/text()")[0]
				except:
					pass
				yield p_info

	# 注册造价师 
	def parse_zczjs(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:
				p_info["reg_num"] = response.xpath("//span[@id='FQualiNumber']/text()")[0]
			except:
				p_info["reg_num"] = None
			try:		
				p_info["nation"] = response.xpath("//span[@id='Fmz']/text()")[0]
			except:
				p_info["nation"] = None
			try:	
				p_info["birthday"] = response.xpath("//span[@id='FBirthDay']/text()")[0]
			except:
				p_info["birthday"] = None
			try:	
				p_info["title"] = response.xpath("//span[@id='FZc']/text()")[0]
			except:
				p_info["title"] = None
			try:	
				p_info["year"] = response.xpath("//span[@id='Fgznx']/text()")[0]
			except:
				p_info["year"] = None
			try:	
				p_info["major"] = response.xpath("//span[@id='Fsxzy']/text()")[0]
			except:
				p_info["major"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
	# 质量检测人员
	def parse_zljcry(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:		
				p_info["title"] = response.xpath("//span[@id='FTitle']/text()")[0]
			except:
				p_info["title"] = None
			try:
				p_info["duty"] = response.xpath("//span[@id='FDuty']/text()")[0]
			except:
				p_info["duty"] = None
			try:
				p_info["worklicense_num"] = response.xpath("//span[@id='FUpCode']/text()")[0]
			except:
				p_info["worklicense_num"] = None
			try:
				p_info["in_date"] = response.xpath("//span[@id='FInDate']/text()")[0]
			except:
				p_info["in_date"] = None
			try:
				p_info["year"] = response.xpath("//span[@id='FYears']/text()")[0]
			except:
				p_info["year"] = None
			try:
				p_info["major"] = response.xpath("//span[@id='FSpecialty']/text()")[0]
			except:
				p_info["major"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info

	# 重庆市监理员
	def parse_cqsjly(self,response):
		#print(response.text)
		data = json.loads(response.text)
		response = etree.HTML(data.get("data"))
		tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
		for tr in tr_list[1:]:
			p_info = PersonInformationItem()
			p_info["name"] = tr.xpath("./td[2]/font/text()")[0]
			p_info["sex"] = tr.xpath("./td[3]/font/text()")[0]
			p_info["company_name"] = tr.xpath("./td[7]/font/text()")[0]
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			p_info["credential_num"] = tr.xpath("./td[4]/font/text()")[0]
			p_info["major"] = tr.xpath("./td[5]/font/text()")[0]
			p_info["major2"] = tr.xpath("./td[6]/font/text()")[0]
			yield p_info
	# 重庆市监理工程师
	def parse_cqsjlgcs(self,response):
		#print(response.text)
		data = json.loads(response.text)
		response = etree.HTML(data.get("data"))
		tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
		for tr in tr_list[1:]:
			p_info = PersonInformationItem()
			p_info["name"] = tr.xpath("./td[2]/font/text()")[0]
			p_info["sex"] = tr.xpath("./td[3]/font/text()")[0]
			p_info["company_name"] = tr.xpath("./td[7]/font/text()")[0]
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			p_info["credential_num"] = tr.xpath("./td[4]/font/text()")[0]
			p_info["major"] = tr.xpath("./td[5]/font/text()")[0]
			p_info["major2"] = tr.xpath("./td[6]/font/text()")[0]
			yield p_info
	# 注册监理工程师
	def parse_zcjlgcs(self,response):
		#print(response.text)
		data = json.loads(response.text)
		response = etree.HTML(data.get("data"))
		tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
		for tr in tr_list[1:]:
			p_info = PersonInformationItem()
			p_info["name"] = tr.xpath("./td[2]/font/a/font/text()")[0]
			p_info["sex"] = tr.xpath("./td[3]/font/text()")[0]
			p_info["company_name"] = tr.xpath("./td[5]/font/text()")[0]
			p_info["credential_num"] = tr.xpath("./td[4]/font/text()")[0]
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
	# 专职安全人员
	def parse_zzaqry(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:			
				p_info["title"] = response.xpath("//span[@id='FJSZC']/text()")[0]
			except:
				p_info["title"] = None
			try:
				p_info["duty"] = response.xpath("//span[@id='FZW']/text()")[0]
			except:
				p_info["duty"] = None
			try:
				p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()")[0]
			except:
				p_info["admissionticket_num"] = None
			try:
				p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()")[0]
			except:
				p_info["aptitude_accept_date"] = None
			try:
				p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()")[0]
			except:
				p_info["aptitude_useful_date"] = None
			try:
				p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()")[0]
			except:
				p_info["credential_num"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
	# 项目安全负责人
	def parse_xmaqfzr(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:			
				p_info["title"] = response.xpath("//span[@id='FJSZC']/text()")[0]
			except:
				p_info["title"] = None
			try:
				p_info["duty"] = response.xpath("//span[@id='FZW']/text()")[0]
			except:
				p_info["duty"] = None
			try:
				p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()")[0]
			except:
				p_info["admissionticket_num"] = None
			try:
				p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()")[0]
			except:
				p_info["aptitude_accept_date"] = None
			try:
				p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()")[0]
			except:
				p_info["aptitude_useful_date"] = None
			try:
				p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()")[0]
			except:
				p_info["credential_num"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
	# 企业安全负责人
	def parse_qyaqfzr(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				p_info["name"] = response.xpath("//span[@id='FName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				p_info["sex"] = response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:
				p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()")[0]
			except:
				p_info["company_name"] = None
			try:
				p_info["title"] = response.xpath("//span[@id='FJSZC']/text()")[0]
			except:
				p_info["title"] = None
			try:
				p_info["duty"] = response.xpath("//span[@id='FZW']/text()")[0]
			except:
				p_info["duty"] = None
			try:
				p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()")[0]
			except:
				p_info["admissionticket_num"] = None
			try:
				p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()")[0]
			except:
				p_info["aptitude_accept_date"] = None
			try:
				p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()")[0]
			except:
				p_info["aptitude_useful_date"] = None
			try:
				p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()")[0]
			except:
				p_info["credential_num"] = None
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
	# 特种作业人员
	def parse_tzzyry(self,response):
		#print(response.text)
		data = json.loads(response.text)
		response = etree.HTML(data.get("data"))
		tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
		for tr in tr_list[1:]:
			p_info = PersonInformationItem()
			p_info["name"] = tr.xpath("./td[2]/font/text()")[0]
			p_info["sex"] = tr.xpath("./td[3]/font/text()")[0]
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			p_info["credential_num"] = tr.xpath("./td[9]/font/text()")[0]
			p_info["aptitude_accept_date"] = tr.xpath("./td[7]/font/text()")[0]
			p_info["aptitude_useful_date"] = tr.xpath("./td[8]/font/text()")[0]
			p_info["handle_type"] = tr.xpath("./td[5]/font/text()")[0]
			p_info["department"] = tr.xpath("./td[6]/font/text()")[0]
			p_info["birthday"] = tr.xpath("./td[4]/font/text()")[0]
			yield p_info
	# 招标代理专职人员
	def parse_zbdlzzry(self,response):
		#print(response.text)
		data = json.loads(response.text)
		html_list = data.get("data")
		for html in html_list:
			response = etree.HTML(html)
			p_info = PersonInformationItem()
			try:
				response.xpath("//span[@id='FFtName']/text()")[0]
			except:
				p_info["name"] = None
			try:
				response.xpath("//span[@id='FSex']/text()")[0]
			except:
				p_info["sex"] = None
			try:			
				p_info["title"] = response.xpath("//span[@id='FTechPost']/text()")[0]
			except:
				p_info["title"] = None
			try:
				response.xpath("//span[@id='FType']/text()")[0]
			except:
				p_info["person_genre"] = None
			try:
				response.xpath("//span[@id='FState']/text()")[0]
			except:
				p_info["status"] = None		
			p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			p_info["is_delete"] = 0
			p_info["mark"] = data.get("mark")
			yield p_info
