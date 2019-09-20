# -*- coding: utf-8 -*-
import pymongo

from scrapy import Request, FormRequest
import datetime
from chongqingpersonproject.items import *
from ..settings import *

class ChongqingpersonSpider(scrapy.Spider):
    name = 'chongqingperson'
    #allowed_domains = ['183.66.171.75:88']
    #注册建造师(由于网站问题，只爬取了一级）
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx']
    # 注册造价师
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx']
    #质量检测人员
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx']
    # 重庆市监理员
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx']
    # 重庆市监理工程师
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx']
    # 注册监理工程师
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx']
    # 专职安全人员(已完成）
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx']
    #项目安全负责人
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx']
    # 企业安全负责人
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx']
    # 特种作业人员
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx']
    # 招标代理专职人员
    #start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx']
    start_urls = ['http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx','http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx']

    def parse(self,response):
        __EVENTTARGET = 'Pager1:LB_Next'
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        # 注册建造师
        if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/zcjzs/Wright_List.aspx":
            formdata = {
                '__VIEWSTATE':__VIEWSTATE,
                'FManageDeptID': '-1',
                'FLevel': '1',
                'FQualiNumber':'',
                'FNumber':'',
                'FIsWright': '-1',
                'BT_Query':'查询'
            }
            yield FormRequest(response.url,formdata=formdata,callback=self.parse_yijijzs)
        else:
            total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
            now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
            #注册造价师
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/zczjs/zczjs_List.aspx":
                mark = "zczjs"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_zczjs, meta={"mark": mark})
            # 质量检测人员
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/zljcry/zljcry_List.aspx":
                mark = "zljcry"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_zljcry, meta={"mark": mark})
            # 重庆市监理员
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/jly/jly_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                if tr_list:
                    for tr in tr_list[1:]:
                        p_info = PersonInformationItem()
                        p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                        p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                        p_info["company_name"] = tr.xpath("./td[7]/font/text()").extract_first()
                        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["is_delete"] = 0
                        p_info["mark"] = "cqsjly"
                        p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                        p_info["major"] = tr.xpath("./td[5]/font/text()").extract_first()
                        p_info["major2"] = tr.xpath("./td[6]/font/text()").extract_first()
                        yield p_info
                else:
                    self.write_error(response)
            # 重庆市监理工程师
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/jlgcs/jlgcs_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                if tr_list:
                    for tr in tr_list[1:]:
                        p_info = PersonInformationItem()
                        p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                        p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                        p_info["company_name"] = tr.xpath("./td[7]/font/text()").extract_first()
                        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["is_delete"] = 0
                        p_info["mark"] = "cqsjlgcs"
                        p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                        p_info["major"] = tr.xpath("./td[5]/font/text()").extract_first()
                        p_info["major2"] = tr.xpath("./td[6]/font/text()").extract_first()
                        yield p_info
                else:
                    self.write_error(response)
            # 注册监理工程师
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/qgzcjlgcs/qgzcjlgcs_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                if tr_list:
                    for tr in tr_list[1:]:
                        p_info = PersonInformationItem()
                        p_info["name"] = tr.xpath("./td[2]/font/a/font/text()").extract_first()
                        p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                        p_info["company_name"] = tr.xpath("./td[5]/font/text()").extract_first()
                        p_info["credential_num"] = tr.xpath("./td[4]/font/text()").extract_first()
                        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["is_delete"] = 0
                        p_info["mark"] = "zcjlgcs"
                        yield p_info
                else:
                    self.write_error(response)
            # 专职安全人员
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/zzaqry/zzaqry_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                mark = "zzaqry"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_zzaqry, meta={"mark": mark})
            # 项目安全负责人
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/xmaqfzr/xmaqfzr_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                mark = "xmaqfzr"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_xmaqfzr, meta={"mark": mark})
            # 企业安全负责人
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/qyaqfzr/qyaqfzr_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                mark = "qyaqfzr"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_qyaqfzr, meta={"mark": mark})
            # 特种作业人员
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/tzry/tzry_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                tr_list = response.xpath("//table[@id='DataGrid1']/tbody/tr")
                if tr_list:
                    for tr in tr_list[1:]:
                        p_info = PersonInformationItem()
                        p_info["name"] = tr.xpath("./td[2]/font/text()").extract_first()
                        p_info["sex"] = tr.xpath("./td[3]/font/text()").extract_first()
                        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        p_info["is_delete"] = 0
                        p_info["mark"] = "tzzyry"
                        p_info["credential_num"] = tr.xpath("./td[9]/font/text()").extract_first()
                        p_info["aptitude_accept_date"] = tr.xpath("./td[7]/font/text()").extract_first()
                        p_info["aptitude_useful_date"] = tr.xpath("./td[8]/font/text()").extract_first()
                        p_info["handle_type"] = tr.xpath("./td[5]/font/text()").extract_first()
                        p_info["department"] = tr.xpath("./td[6]/font/text()").extract_first()
                        p_info["birthday"] = tr.xpath("./td[4]/font/text()").extract_first()
                        yield p_info
                else:
                    self.write_error(response)
            # 招标代理专职人员
            if response.url == "http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/zbdlcyry_List.aspx":
                __EVENTTARGET = 'TurnPage1:LB_Next'
                __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
                total_page = response.xpath("//span[@id='TurnPage1_pagecount']/text()").extract_first()
                now_page = response.xpath("//span[@id='TurnPage1_currentpage']/text()").extract_first()
                mark = "zbdlzzry"
                tr_list = response.xpath("//table[@id='DataGrid1']/tr")
                for tr in tr_list[1:]:
                    href = tr.xpath("./td[2]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
                    formdata = {
                        '__EVENTTARGET': href,
                        '__VIEWSTATE': __VIEWSTATE,
                        'FManageDeptID': '-1',
                        'FLevel': '0',
                        'FIsWright': '-1'
                    }
                    yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle, meta={"mark": mark})

            request = self.next_page(response,now_page,total_page,__VIEWSTATE,__EVENTTARGET)
            yield request
    # 一级建造师
    def parse_yijijzs(self,response):
        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract_first()
        total_page = response.xpath("//span[@id='Pager1_Pages']/text()").extract_first()
        now_page = response.xpath("//span[@id='Pager1_CPage']/text()").extract_first()
        mark = "zcjzs"
        tr_list = response.xpath("//table[@id='DataGrid1']/tr")
        for tr in tr_list[1:]:
            href = tr.xpath("./td[1]/font/a/@href").extract_first().strip().split("'")[1].replace("$", ":")
            name = tr.xpath("./td[1]/font/a/font/text()").extract_first()
            formdata = {
                '__EVENTTARGET': href,
                '__VIEWSTATE': __VIEWSTATE,
                'FManageDeptID': '-1',
                'FLevel': '1',
                'FIsWright': '-1'
            }
            yield FormRequest(response.url, formdata=formdata, callback=self.parse_middle, meta={"mark": mark})
        if int(total_page) > int(now_page):
            # if int(now_page) < 6:
            formdata_n = {
                '__EVENTTARGET': 'Pager1:LB_Next',
                '__VIEWSTATE': __VIEWSTATE,
                'FManageDeptID': '-1',
                'FLevel': '1',
                'FIsWright': '-1'
            }
            yield FormRequest(response.url, formdata=formdata_n, callback=self.parse_yijijzs)
    # 下一页
    def next_page(self,response,now_page,total_page,__VIEWSTATE,__EVENTTARGET):
        if int(total_page) > int(now_page):
        #if int(now_page) < 6:
            formdata_n = {
                '__EVENTTARGET': __EVENTTARGET,
                '__VIEWSTATE': __VIEWSTATE,
                'FManageDeptID': '-1',
                'FLevel': '0',
                'FIsWright': '-1'
            }
            return FormRequest(response.url, formdata=formdata_n, callback=self.parse)
    #中间
    def parse_middle(self,response):
        mark = response.meta.get("mark")
        if mark == "zcjzs":
            url = "http://183.66.171.75:88" + response.xpath("//script[1]/text()").extract_first().split("'")[1]
            yield Request(url, callback=self.parse_zcjzs, meta={"mark": mark})
        if mark == "zbdlzzry":
            url = "http://183.66.171.75:88/CQCollect/Ry_Query/zbdlcyry/" + response.xpath("//script[1]/text()").extract_first().split("'")[1]
            yield Request(url, callback=self.parse_zbdlzzry, meta={"mark": mark})
    # 注册建造师
    def parse_zcjzs(self,response):
            #二级
            # p_info = PersonInformationItem()
            # p_info["name"] = response.xpath("//span[@id='_FName']/text()").extract_first()
            # p_info["sex"] = response.xpath("//span[@id='_FSex']/text()").extract_first()
            # p_info["company_name"] = response.xpath("//span[@id='_FBaseinfoName']/text()").extract_first()
            # p_info["reg_num"] = response.xpath("//span[@id='_FNumber']/text()").extract_first()
            # p_info["seal_num"] = response.xpath("//span[@id='_FVerifyNumber']/text()").extract_first()
            # p_info["reg_credential_num"] = response.xpath("//span[@id='_FQNumber']/text()").extract_first()
            # p_info["aptitude_useful_date"] = response.xpath("//span[@id='_FValidDate']/text()").extract_first()
            # p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # p_info["is_delete"] = 0
            # p_info["mark"] = response.meta.get("mark")
            # p_info["url"] = response.url
            # p_info["department"] = response.xpath("//span[@id='_FManageDeptName']/text()").extract_first()
            # # try:
            # tr_list = response.xpath("//table[@id='DataGrid1']/tr")
            # if len(tr_list) > 1:
            #     for tr in tr_list[1:]:
            #         p_info["credential_num"] = tr.xpath("./td[2]/text()").extract_first()
            #         p_info["aptitude_speciality"] = tr.xpath("./td[1]/text()").extract_first()
            #         p_info["aptitude_accept_date"] = tr.xpath("./td[3]/text()").extract_first()
            #         yield p_info
            # else:
            #     p_info["sex"] = response.xpath("//span[@id='_FSex']/font/text()").extract_first()
            #     p_info["credential_num"] = response.xpath("//span[@id='_FQNumber']/text()").extract_first()
            #     p_info["title_level"] = response.xpath("//table[@id='Table5']/tr[10]/td[4]/text()").extract_first().strip()
            #     yield p_info
            #一级
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        p_info["major"] = response.xpath("//span[@id='FQualiName']/text()").extract_first()
        p_info["aptitude_speciality"] = response.xpath("//span[@id='FQualiName']/text()").extract_first()
        p_info["title_level"] = response.xpath("//span[@id='FLevel']/text()").extract_first()
        p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        p_info["reg_num"] = response.xpath("//span[@id='FNumber']/text()").extract_first()
        p_info["reg_credential_num"] = response.xpath("//span[@id='FQualiNumber']/text()").extract_first()
        p_info["aptitude_useful_date"] = response.xpath("//span[@id='FValidDate']/text()").extract_first()
        p_info["aptitude_accept_date"] = response.xpath("//span[@id='FDate4']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["nation"] = response.xpath("//span[@id='FNation']/text()").extract_first()
        p_info["birthday"] = response.xpath("//span[@id='FBirthdate']/text()").extract_first()
        p_info["department"] = response.xpath("//span[@id='FManageDeptName']/text()").extract_first()
        p_info["person_type"] = "注册建造师"
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        yield p_info
    # 注册造价师
    def parse_zczjs(self,response):
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        p_info["reg_num"] = response.xpath("//span[@id='FQualiNumber']/text()").extract_first()
        p_info["nation"] = response.xpath("//span[@id='Fmz']/text()").extract_first()
        p_info["birthday"] = response.xpath("//span[@id='FBirthDay']/text()").extract_first()
        p_info["title"] = response.xpath("//span[@id='FZc']/text()").extract_first()
        p_info["year"] = response.xpath("//span[@id='Fgznx']/text()").extract_first()
        p_info["major"] = response.xpath("//span[@id='Fsxzy']/text()").extract_first()
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        p_info["person_type"] = "注册造价师"
        yield p_info
    # 质量检测人员
    def parse_zljcry(self,response):
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        p_info["title"] = response.xpath("//span[@id='FTitle']/text()").extract_first()
        p_info["duty"] = response.xpath("//span[@id='FDuty']/text()").extract_first()
        p_info["worklicense_num"] = response.xpath("//span[@id='FUpCode']/text()").extract_first()
        p_info["in_date"] = response.xpath("//span[@id='FInDate']/text()").extract_first()
        p_info["year"] = response.xpath("//span[@id='FYears']/text()").extract_first()
        p_info["major"] = response.xpath("//span[@id='FSpecialty']/text()").extract_first()
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        p_info["person_type"] = "质量检测人员"
        yield p_info
    # 专职安全人员
    def parse_zzaqry(self,response):
            p_info = PersonInformationItem()
            p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
            p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
            p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
            p_info["title"] = response.xpath("//span[@id='FJSZC']/text()").extract_first()
            p_info["duty"] = response.xpath("//span[@id='FZW']/text()").extract_first()
            p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()").extract_first()
            p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()").extract_first()
            p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()").extract_first()
            p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()").extract_first()
            p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            p_info["is_delete"] = 0
            p_info["mark"] =response.meta.get("mark")
            p_info["url"] = response.url
            p_info["person_type"] = "专职安全人员"
            yield p_info
    # 项目安全负责人
    def parse_xmaqfzr(self,response):
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        p_info["title"] = response.xpath("//span[@id='FJSZC']/text()").extract_first()
        p_info["duty"] = response.xpath("//span[@id='FZW']/text()").extract_first()
        p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()").extract_first()
        p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()").extract_first()
        p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()").extract_first()
        p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()").extract_first()
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        p_info["person_type"] = "项目安全负责人"
        yield p_info
    # 企业安全负责人
    def parse_qyaqfzr(self,response):
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FName']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["company_name"] = response.xpath("//span[@id='FBaseinfoName']/text()").extract_first()
        p_info["title"] = response.xpath("//span[@id='FJSZC']/text()").extract_first()
        p_info["duty"] = response.xpath("//span[@id='FZW']/text()").extract_first()
        p_info["admissionticket_num"] = response.xpath("//span[@id='FZKZH']/text()").extract_first()
        p_info["aptitude_accept_date"] = response.xpath("//span[@id='FFZRQ']/text()").extract_first()
        p_info["aptitude_useful_date"] = response.xpath("//span[@id='FYXQA']/text()").extract_first()
        p_info["credential_num"] = response.xpath("//span[@id='FZSBH']/text()").extract_first()
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        p_info["person_type"] = "企业安全负责人"
        yield p_info
    # 招标代理专职人员
    def parse_zbdlzzry(self,response):
        p_info = PersonInformationItem()
        p_info["name"] = response.xpath("//span[@id='FFtName']/text()").extract_first()
        p_info["sex"] = response.xpath("//span[@id='FSex']/text()").extract_first()
        p_info["title"] = response.xpath("//span[@id='FTechPost']/text()").extract_first()
        p_info["person_genre"] = response.xpath("//span[@id='FType']/text()").extract_first()
        p_info["status"] = response.xpath("//span[@id='FState']/text()").extract_first()
        p_info["create_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["modification_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        p_info["is_delete"] = 0
        p_info["mark"] = response.meta.get("mark")
        p_info["url"] = response.url
        p_info["person_type"] = "招标代理专职人员"
        yield p_info
    def write_error(self,response):
        myclient = pymongo.MongoClient('mongodb://ecs-a025-0002:27017/')
        mydb = myclient[MONGODATABASE]
        mycol = mydb[MONGOTABLE]
        mydict = {"url": response.url, "reason": "该页未返回数据", 'text': response.text,'spider':'chongqingperson','time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        mycol.insert_one(mydict)
        myclient.close()
