from baike_crawler_py3 import html_downloader
from baike_crawler_py3 import html_outputer
from baike_crawler_py3 import html_parser
from baike_crawler_py3 import url_manager

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count=1
        #添加到新URL库中
        self.urls.add_new_url(root_url)
        #
        while self.urls.has_new_url():
            try:
                #获取一个新的链接
                new_url=self.urls.get_new_url()
                #打印 序号以及链接
                print('craw： %d:%s'%(count,new_url))
                #下载链接内容
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                #添加新的url链接到 新URL库
                self.urls.add_new_urls(new_urls)
                #输出内容到html中
                self.outputer.collect_data(new_data)
                if count==100:
                    break
                count=count+1
            except:
                print('craw faild!!')
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
