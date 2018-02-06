# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:44:36 2018

@author: Liunux
"""

import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from CnblogsSpider.items import CnblogsspiderItem

class CnblogsSpider(scrapy.Spider):
    name="cnblogs"
    allowed_domains=["cnblogs.com"]
    start_urls=[
            "http://www.cnblogs.com/qiyeboy/default.html"
            ]
    def parse(self,response):
        #首先抽取所有文章
        papers=response.xpath(".//*[@class='day']")
        #从每篇文章中抽取数据
        for paper in papers:
            url=paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title=paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time=paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content=paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            #print(url,title,time,content)
            item=CnblogsspiderItem(url=url,title=title,time=time,content=content)
            request=scrapy.Request(url=url,callback=self.parse_body)
            request.meta['item']=item  #将item暂存
            yield request
        
        next_page=Selector(response).re(u'<a href="(\S*)">下一页</a>')
        #next_page得到下一页url
        if next_page:
            yield scrapy.Request(url=next_page[0],callback=self.parse)

    def parse_body(self,response):
        item=response.meta['item']
        body=response.xpath(".//*[@class='postBody']")
        item['cimage_urls']=body.xpath(".//img/@src").extract()
        yield item
        
        
if __name__=='__main__':
    process=CrawlerProcess({
            'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
            })
    process.crawl(CnblogsSpider)
    process.start()
