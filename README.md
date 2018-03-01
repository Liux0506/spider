# spider
Python爬虫-Scrapy框架
1. 安装
pip install Scrapy

问题：
pip install Scrapy报错
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
解决：
http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted  下载twisted对应版本的whl文件，cp后面是python版本，amd64代表64位，运行命令：
pip install D:\_Liunux\study\python\Twisted-17.9.0-cp36-cp36m-win_amd64.whl
成功安装后再运行
pip install Scrapy  
安装成功


2. 新建项目
在命令行，切换的自己的项目代码的工作空间下，执行如下命令
cd D:\_Liunux\study\python\Project
scrapy startproject ScrapyTest


3.spider运行流程
Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。 换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。
对spider来说，爬取的循环类似下文:
1) 以初始的URL初始化Request，并设置回调函数。 当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。
2) spider中初始的request是通过调用 start_requests() 来获取的。 start_requests() 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request 。
3) 在回调函数内分析返回的(网页)内容，返回 Item 对象或者 Request 或者一个包括二者的可迭代容器。 返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。
4) 在回调函数内，您可以使用 选择器(Selectors) (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item。
最后，由spider返回的item将被存到数据库(由某些 Item Pipeline 处理)或使用 Feed exports 存入到文件中。
