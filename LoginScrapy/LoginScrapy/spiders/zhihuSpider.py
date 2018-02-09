# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 17:59
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : zhihuSpider.py
# @Software: PyCharm

import scrapy

class zhihuSpider(scrapy.Spider):
    name='zhihu'
    allowed_domain=["www.zhihu.com"]
    start_urls=["https://www.zhihu.com/signup?next=%2F"]

    header={
        "Host":"www.zhihu.com",
        "Connection": "keep-alive",
        "accept:"*/*",
        "authorization":"Bearer 2|1:0|10:1517997746|4:z_c0|92:Mi4xbGF3MEFBQUFBQUFBQUd5UktRRWNEU1lBQUFCZ0FsVk5zaHhvV3dCeFFscXFKZFJsMjZnMlRUN3VFQ3dTdWROLWhn|867ba72df36043de8ab78a35922a94821d13d9c206d41802398e0ec82b3a6262",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Referer": "https://www.zhihu.com/",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    cookie={
        "aliyungf_tc": "AQAAAN5B3xULiAgAZtYQDhsQxZZZdNCS",
        "capsion_ticket":"2 | 1:0 | 10: 1517997708 | 14:capsion_ticket | 44: MjdhM2FjOTBiMjhjNDRhNGE3ODdjZTcwZTBlN2I2ODA = | ceeec4d332fe93333912cae18a8ec4d65cb98f25b1340eb5cf2a016efeb9b1c9",
        "z_c0":"2 | 1: 0 | 10:1517997746 | 4: z_c0 | 92:Mi4xbGF3MEFBQUFBQUFBQUd5UktRRWNEU1lBQUFCZ0FsVk5zaHhvV3dCeFFscXFKZFJsMjZnMlRUN3VFQ3dTdWROLWhn | 867ba72df36043de8ab78a35922a94821d13d9c206d41802398e0ec82b3a6262",
        "_xsrf": "cdd760ed-d178-4722-a34c-40b73052be8b",
        "q_c1": "36399dfc6cb24bd7a031901dfba12dc8|1517997746000|1517997746000"
     }

    def start_requests(self):
        return scrapy.http.FormRequest(url=self.start_urls,headers=header,cookies=cookie,meta={"cookiejar":1},callback=self.post_login)

    def post_login(self, response):



