# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse,TextResponse
from selenium.common.exceptions import TimeoutException
from lxml import etree
import json
from scrapy.conf import settings
driver_path = settings.get("DRIVERPATH")
deal_js = "document.getElementById('ad1').parentNode.removeChild(document.getElementById('ad1'))"
class SeleniumMiddleware():
	def __init__(self):
		self.chrome_options = Options()
		self.chrome_options.add_argument('--headless')
		self.driver = webdriver.Chrome(chrome_options=self.chrome_options,executable_path  = driver_path)
		self.wait = WebDriverWait(self.driver,20)
	def process_request(self,request,spider):
		if request.meta.get("mark") in ["zczjs","zljcry","zzaqry","qyaqfzr","xmaqfzr"]:
			self.driver.get(request.url)
			num = request.meta.get("num")
			if num:
				go = self.driver.find_element_by_id(request.meta.get("go"))
				page = self.driver.find_element_by_id(request.meta.get("page"))
				self.driver.execute_script(deal_js)
				page.send_keys(num)
				go.click()
				html_list = []
				for i in range(2,23):
					try:
						tr = self.driver.find_element_by_xpath("//table[@id='DataGrid1']/tbody/tr[{}]/td[{}]/font/a".format(i,request.meta.get("line")))
						self.driver.execute_script(deal_js)
						tr.click()
						html_list.append(self.driver.page_source)
						self.driver.back()
					except:
						break
				msg = {"data":html_list,"mark":request.meta.get("mark")}
				return HtmlResponse(url=request.url, body=json.dumps(msg,ensure_ascii=False),encoding='utf-8',request=request,status=200)
		if request.meta.get("mark") in ["cqsjly","cqsjlgcs","zcjlgcs","tzzyry"]:
			self.driver.get(request.url)
			num = request.meta.get("num")
			if num:
				go = self.driver.find_element_by_id(request.meta.get("go"))
				page = self.driver.find_element_by_id(request.meta.get("page"))
				self.driver.execute_script(deal_js)
				page.send_keys(num)
				go.click()
				html = self.driver.page_source
				msg = {"data":html,"mark":request.meta.get("mark")}
				return HtmlResponse(url=request.url, body=json.dumps(msg,ensure_ascii=False),encoding='utf-8',request=request,status=200)
		if request.meta.get("mark") in ["zcjzs","zbdlzzry"]:
			self.driver.get(request.url)
			num = request.meta.get("num")
			if num:
				go = self.driver.find_element_by_id(request.meta.get("go"))
				page = self.driver.find_element_by_id(request.meta.get("page"))
				self.driver.execute_script(deal_js)
				page.send_keys(num)
				go.click()
				html_list = []
				for i in range(2,23):
					try:
						tr = self.driver.find_element_by_xpath("//table[@id='DataGrid1']/tbody/tr[{}]/td[{}]/font/a".format(i,request.meta.get("line")))
						self.driver.execute_script(deal_js)
						tr.click()
						windows = self.driver.window_handles
						self.driver.switch_to.window(windows[-1])
						html_list.append(self.driver.page_source)
						self.driver.close()
						windows = self.driver.window_handles
						self.driver.switch_to.window(windows[-1])
					except:
						break
				msg = {"data":html_list,"mark":request.meta.get("mark")}
				return HtmlResponse(url=request.url, body=json.dumps(msg,ensure_ascii=False),encoding='utf-8',request=request,status=200)