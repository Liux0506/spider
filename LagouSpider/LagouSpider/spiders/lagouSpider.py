# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:38:03 2018

@author: Liunux
"""

import scrapy
from LagouSpider.items import LagouspiderItem
from scrapy.crawler import CrawlerProcess


class lagouSpider(scrapy.Spider):
    name = "lagou"
    start_urls = ["https://www.lagou.com"]
    cookie={"Cookie:_ga":"GA1.2.808020733.1470503871",
            "user_trace_token":"20160807011749-b38978c8-5bf9-11e6-83a4-525400f775ce",
            "LGUID":"20160807011749-b3897d06-5bf9-11e6-83a4-525400f775ce",
            "showExpriedIndex":"1",
            "showExpriedCompanyHome":"1",
            "showExpriedMyPublish":"1",
            "hasDeliver":"0",
            "index_location_city":"%E5%B9%BF%E5%B7%9E",
            "JSESSIONID":"ABAAABAAAIAACBI301E0F239534F71E371F4AE4F384A8BF",
            "_gid":"GA1.2.1663004256.1517311444",
            "TG-TRACK-CODE":"index_navigation",
            "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6":1516842428,
            "X_HTTP_TOKEN":"25ac7f995298636d86c70e37db93b51c",
            "gate_login_token":"",
            "LGSID":"20180201100607-77434dfa-06f4-11e8-abe2-5254005c3644",
            "PRE_UTM":"",
            "PRE_HOST":"",
            "PRE_SITE":"https%3A%2F%2Fwww.lagou.com%2F",
            "PRE_LAND":"https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fts%3D1517450766216%26serviceId%3Dlagou%26service%3Dhttps%25253A%25252F%25252Fwww.lagou.com%25252F%26action%3Dlogin%26signature%3D2A2930CA8161C1718E2ECC72E7695328",
            "_putrc":"234EED094EF36710",
            "login":"true",
            "unick":"%E5%88%98%E6%B5%94",
            "gate_login_token":"722507fdf0ebb3ea01b91c8531a713b13180dc66f9034e11",
            "_gat":1,
            "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6":1517450992,
            "LGRID":"20180201100949-fb25776b-06f4-11e8-abe2-5254005c3644"
        }
    def parse(self, response):
        # classList=response.xpath("//div[@class='menu_box']/div/div/a")
        classList = response.xpath("//div[@class='menu_box']/div/dl/dd/a")
        # print (classList[0])
        for item in classList:
            jobClass = item.xpath("text()").extract()
            jobUrl = item.xpath("@href").extract()[0]
            item = LagouspiderItem(jobClass=jobClass, jobUrl=jobUrl)
            request = scrapy.Request(url=jobUrl, cookies=self.cookie, meta={"jobClass": jobClass,"jobUrl":jobUrl}, callback=self.parse_body)
            yield request

    def parse_body(self, response):
        jobClass = response.meta["jobClass"]
        jobUrl = response.meta["jobUrl"]
        # ['https://www.lagou.com/zhaopin/Java/']
        print("this is parse_body")
        jobList = response.xpath("//ul[@class='item_con_list']/li")
        for item in jobList:
            jobName = item.xpath('div/div/div/a/h3/text()').extract()[0]
            jobPlace = item.xpath('div/div/div/a/span/em/text()').extract()
            jobMoney = item.xpath('div/div/div/div/span/text()').extract()
            jobNeed = item.xpath('div/div/div/div/text()').extract()
            jobNeed = jobNeed[2].strip()
            jobCompany = item.xpath('div/div/div/a/text()').extract()
            jobCompany = jobCompany[3].strip()

            jobType = item.xpath('div/div/div/text()').extract()
            jobType = jobType[7].strip()

            jobSpesk = item.xpath('div[@class="list_item_bot"]/div/text()').extract()
            jobSpesk = jobSpesk[-1].strip()

            Item = LagouspiderItem()
            Item["jobClass"] = jobClass
            Item["jobUrl"] = jobUrl
            Item["jobName"] = jobName
            Item["jobPlace"] = jobPlace
            Item["jobMoney"] = jobMoney
            Item["jobNeed"] = jobNeed
            Item["jobCompany"] = jobCompany
            Item["jobType"] = jobType
            Item["jobSpesk"] = jobSpesk
            # print(oneItem["jobName"])
            yield Item


from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class lagou2Spider(scrapy.Spider):
    name = 'lagou2'
    start_urls = ["https://www.lagou.com/login"]

    def __init__(self):
        ##设置模拟的浏览器
        self.brower = webdriver.chrome(executable_path="D:/_Liunux/study/python/Project/chromedriver.exe")
        super(lagou2Spider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候 关闭chrome
        print("spider closed")
        # self.browser.quit()

    def parse(self, response):
        print(response.body.decode)

# from scrapy.crawler import CrawlerProcess
# if __name__=='__main__':
#     process=CrawlerProcess({
#             'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
#             })
#     process.crawl(lagouSpider)
#     process.start()