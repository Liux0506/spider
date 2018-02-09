scrapy模拟登陆
参考：
https://brantou.github.io/2017/08/22/scrapy-crawl-zhihu/

1.进入登录页，获取 Header 和 Cookie 信息。
完善的 Header 信息能尽量伪装爬虫， 有效 Cookie 信息能迷惑知乎服务端，使其认为当前登录非首次登录，若无有效 Cookie 会遭遇验证码。 在抓取数据之前，请在浏览器中登录过知乎，这样才使得 Cookie 是有效的。
2.

1.Request中meta参数
作用是传递信息给下一个函数，使用过程可以理解成：
把需要传递的信息赋值给这个叫meta的变量，但meta只接受字典类型的赋值，因此要把待传递的信息改成“字典”的形式，即：
meta={'key1':value1,'key2':value2}
如果想在下一个函数中取出value1,只需得到上一个函数的meta['key1']即可，因为meta是随着Request产生时传递的，下一个函数得到的Response对象中就会有meta，
即response.meta，取value1则是value1=response.meta['key1']

2.cookiejar
meta当然是可以传递cookie的（第一种）：下面start_requests中键‘cookiejar’是一个特殊的键，scrapy在meta中见到此键后，会自动将cookie传递到要callback的函数中。既然是键(key)，就需要有值(value)与之对应，例子中给了数字1，也可以是其他值，比如任意一个字符串。
def start_requests(self):
    yield Request(url,meta={'cookiejar':1},callback=self.parse)
需要说明的是，meta给‘cookiejar’赋值除了可以表明要把cookie传递下去，还可以对cookie做标记。一个cookie表示一个会话(session)，如果需要经多个会话对某网站进行爬取，可以对cookie做标记，1,2,3,4......这样scrapy就维持了多个会话。
