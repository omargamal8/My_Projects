from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.item import Item, Field


class TextPostItem(Item):
    Org_Link = Field()
    Count=Field()
   # highlight = Field()
    #rest= Field()

class RedditCrawler(CrawlSpider):
    name = 'crawler'
    myfile = open("D:\ext.txt" , "r")
    links= myfile.readlines()
    myfile.close()
    allowed_domains = ['https://summerofcode.withgoogle.com/']
    start_urls = links
    custom_settings = {
            'BOT_NAME': 'scraper',
            'DEPTH_LIMIT': 7,
            'DOWNLOAD_DELAY': 1
            }

    def parse(self, response):
        keywords=["java","javascript","java script", "c++","c#","python","qt","c#/c++","c/c++","github","gitlab","git lab", "git hub"]
        s = Selector(response)
        techelements = Selector(response).xpath('/html/body/main/section[1]/div/div/div[2]/md-card/div/div[3]/ul/li')
        counter=0
        hit_counter=0

        print ("There is "+str(len(techelements))+" Technologies used")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FFFFFFFFFLAAAAAAAAAAAAAAAG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        myfile = open("D:\ext.txt" , "r")
        links= myfile.readlines()
        myfile.close()
        for techelement in techelements:

            tech = techelement.xpath('text()').extract()[0]
            print ("el kelma :\n\n")
            print tech,len(tech)
            print ("\n\n")
            if(tech.lower() in keywords):
              hit_counter+=1

        if(hit_counter>=len(techelements)-2):
              i=TextPostItem()
              i['Org_Link']=response.url
              i['Count']=(str(hit_counter)+"/"+str(len(techelements)))
              yield i      

              
            #print("<<<<<<<<><><><><>>>>>>>>>>>>"+str(tech))
            #print("\n\n")
           # i['highlight'] = post.xpath('strong/text()').extract()
           # i['rest'] = post.xpath('text()[2]').extract()[0]
            

       # negativeposts = Selector(response).xpath('//div[@class="box-pros-and-cons mb-rm"]/ul/li[2]')
 
      #  for post in negativeposts:
      #      i = TextPostItem()
       #     i['comment'] = post.xpath('blockquote[@class="quote"]/text()').extract()[0]
      #      i['highlight'] = post.xpath('blockquote[@class="quote"]/strong/text()').extract()[0]
        #    i['rest'] = post.xpath('blockquote[@class="quote"]/text()[2]').extract()[0]
        #    yield i            