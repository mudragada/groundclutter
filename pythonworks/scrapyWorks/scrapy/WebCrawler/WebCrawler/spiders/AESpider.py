# -*- coding: utf-8 -*-
import scrapy, re, time, datetime, urlparse, random
from scrapy.selector import Selector
from WebCrawler.items import WebHttpResponse
from WebCrawler.utils import UrlUtils

class WebSpider(scrapy.Spider):
	def __init__(self):
		self.timeStamp = int(datetime.datetime.now().strftime("%s")) * 1000
		self.urlUtilsObj = UrlUtils()
		self.parsedPageDict = dict()
		# self.parsedProdDict = dict()
	
	## Identifies the spider
	name = "AESpider"
	allowed_domains = ["www.ae.com"]
	start_urls = ['https://www.ae.com']
	start_url = start_urls[0]
	def start_requests(self):
		for homePageUrl in self.start_urls:
			yield scrapy.Request(homePageUrl)

	def parse(self, response):
		return self.parseTopNavUrls(response)
	
	def parseTopNavUrls(self, response):
		responseSelector = Selector(response)
		topNavSelectorList = responseSelector.xpath(self.settings.get('XPATH_TOPNAV_URL'))
		for topNavUrl in topNavSelectorList:
			targetUrl = str(topNavUrl.xpath('@href').extract_first())
			if(self.urlUtilsObj.getPageType(targetUrl) != ""):
				yield scrapy.Request(urlparse.urljoin(self.start_url, targetUrl), callback=self.extractCatAndProdUrls)

	def extractCatAndProdUrls(self, response):
		yield self.extractPageData(response)
		responseSelector = Selector(response)
		categorySelectorList = responseSelector.xpath(self.settings.get('XPATH_CAT_URL'))
		productSelectorList = responseSelector.xpath(self.settings.get('XPATH_PROD_URL'))

		urlList = categorySelectorList + productSelectorList
		random.shuffle(urlList)
		for unicodeUrl in urlList:
			url = str(unicodeUrl.xpath('@href').extract_first())
			targetId = self.urlUtilsObj.getIdFromUrl(url)
			if(targetId != ""):
				targetUrl = urlparse.urljoin(self.start_url, url)
				if(self.parsedPageDict.get(targetId) == None or self.parsedPageDict.get(targetId) == 1):
					yield scrapy.Request(targetUrl, callback=self.extractCatAndProdUrls)

	
	def extractPageData(self, response):
		targetUrl = response.url
		self.addToParsedDict(self.urlUtilsObj.getIdFromUrl(targetUrl))
		responseItem = AEHttpResponse()
		responseItem['response'] = response
		responseItem['timeStamp'] = self.timeStamp
		responseItem['startUrl'] = self.start_url
		return responseItem

	def addToParsedDict(self, id):
		if id in self.parsedPageDict:
			count = self.parsedPageDict[id] + 1
		else:
			count = 1
		self.parsedPageDict[id] = count


		






