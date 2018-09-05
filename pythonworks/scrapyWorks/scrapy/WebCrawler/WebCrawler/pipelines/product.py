from AECrawler.items import AEProductItem
from AECrawler.utils import UrlUtils
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class ProductInfoPipeline(object):
	def __init__(self):
		self.settings = get_project_settings()
		self.urlUtilsObj = UrlUtils()
	
	def process_item(self, item, spider):
		if(item != None):
			response = item['response']
			if (self.urlUtilsObj.getPageType(response.url) == self.settings.get('PRODUCT_PAGE_TYPE')):
				self.timeStamp = item['timeStamp']
				return self.parseProductResponse(response)
			else:
				return item

	def parseProductResponse(self, response):
		prodItem = AEProductItem()
		prodItem['url'] = self.urlUtilsObj.trimUrlParams(response.url)
		prodItem['productId'] = self.urlUtilsObj.getIdFromUrl(response.url)
		prodItem['size'] = int(len(response.body))
		prodItem['timeStamp'] = self.timeStamp
		prodItem['responseCode'] = response.status
		prodItem['productName'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_NAME')
		prodItem['productAvailability'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_AVAILABILITY')
		prodItem['listPrice'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_LIST_PRICE')
		prodItem['salePrice'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_SALE_PRICE')
		prodItem['pspDiscountText'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_DISCOUNT_TEXT')
		prodItem['pspPromoText'] = self.urlUtilsObj.getXPathStr(response, 'XPATH_PRODUCT_PAGE_PROMO_TEXT')

		print(prodItem)