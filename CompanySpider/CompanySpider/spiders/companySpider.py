import scrapy
from scrapy.crawler import CrawlerProcess
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from CompanySpider.items import CompanyspiderItem
class companySpider(scrapy.Spider):
    name = "qichacha"
    #allowed_domains = ["www.tianyancha.com"]
    start_urls = ["http://www.qichacha.com/g_GD"]
    #"http://www.qichacha.com" http://www.qichacha.com/user_login

    handle_httpstatus_list = [405]
    keys = ["江西天人生态股份有限公司", "深圳市海信通国际投资有限公司", "深圳市富通达车库有限公司"]


    def parse(self, response):
        for key in self.keys:
            self.driver = webdriver.Chrome(executable_path="D:/_Liunux/study/python/chromedriver.exe")
            self.driver.get(self.start_urls[0])
            serchkey = self.driver.find_element_by_id("headerKey")
            serchkey.clear()
            serchkey.send_keys(key)
            serchbtn = self.driver.find_element_by_xpath("/html/body/header/div/form/div/div/span/button")
            serchbtn.click()
            sel = scrapy.Selector(text=self.driver.page_source)
            itemList = sel.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]')
            print (itemList)
            self.driver.close()
            for i in itemList:
                item = CompanyspiderItem()
                item["companyName"] = i.xpath('//*[@id ="searchlist"]/table/tbody/tr[1]/td[2]/a/em/em/text()').extract()
                item["companyPerson"] = i.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/p[1]/a/text()').extract()
                # print(item)
                yield item
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
