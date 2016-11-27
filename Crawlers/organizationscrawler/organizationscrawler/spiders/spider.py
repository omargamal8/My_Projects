from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.item import Item, Field


class TextPostItem(Item):
    link = Field()
   # highlight = Field()
    #rest= Field()

class RedditCrawler(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['https://summerofcode.withgoogle.com/']
    start_urls = ['https://summerofcode.withgoogle.com/archive/2016/organizations/']
    custom_settings = {
            'BOT_NAME': 'scraper',
            'DEPTH_LIMIT': 7,
            'DOWNLOAD_DELAY': 3
            }

    def parse(self, response):
        s = Selector(response)
        positiveposts = Selector(response).xpath('/html/body/main/section/div/ul/li/a')


        for post in positiveposts:
            
            i = TextPostItem()
            print post
            i['link'] = post.xpath('@href').extract()
            print (">>>>>>>>>>>>>>>>>>>>>>>"+str(post.xpath('/a/@href').extract()))
           # i['highlight'] = post.xpath('strong/text()').extract()
           # i['rest'] = post.xpath('text()[2]').extract()[0]
            yield i

       # negativeposts = Selector(response).xpath('//div[@class="box-pros-and-cons mb-rm"]/ul/li[2]')
 
      #  for post in negativeposts:
      #      i = TextPostItem()
       #     i['comment'] = post.xpath('blockquote[@class="quote"]/text()').extract()[0]
      #      i['highlight'] = post.xpath('blockquote[@class="quote"]/strong/text()').extract()[0]
        #    i['rest'] = post.xpath('blockquote[@class="quote"]/text()[2]').extract()[0]
        #    yield i            