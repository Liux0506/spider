# spider
Python爬虫-Scrapy
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

