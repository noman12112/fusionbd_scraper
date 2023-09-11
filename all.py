from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import scrapy
import re

class Fusion(CrawlSpider):
	name = "fusionspider"
	start_urls = [ 'http://books.fusionbd.com/index.php?sort=1',
 'http://page.fusionbd.com/mp3.html',
 'http://radiospecials.fusionbd.com/index.php?sort=1&p=1',
 'http://page.fusionbd.com/3gpvideos.html',
 'http://mp4videos.fusionbd.com/index.php?dir=320x240_Pixels&sort=1&p=1',
 'http://mp4videos.fusionbd.com/index.php?dir=640x480_Pixels&p=1&sort=1',
 'http://mp4videos.fusionbd.com/index.php?dir=/1080x720_Pixels-HD&p=1&sort=1',
 'http://mtube.fusionbd.com',
 'http://newnatok.fusionbd.com/index.php?dir=Natok_And_Telefilms&p=1&sort=1',
 'http://movies.fusionbd.com/index.php?p=1&sort=1']
	rules = (Rule(LinkExtractor(restrict_xpaths='//div[@class="fl odd"]'),callback = "parse",follow=True),)
	
	def parse(self,response):
		ls =[ i.url for i in  LinkExtractor(allow='').extract_links(response)]
		for i in ls:
			if re.compile('file').search(i):
				yield response.follow(i,callback=self.fileparse)

	def fileparse(self,response):
		url = response.urljoin(response.xpath('/html/body/h2[2]/a/@href').get())
		name = url.split('/')[-1]
		yield{
			"name":name,
			"url":url
					}
