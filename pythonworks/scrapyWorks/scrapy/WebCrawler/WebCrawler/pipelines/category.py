from AECrawler.items import AECategoryItem
from AECrawler.utils import UrlUtils
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

class CategoryInfoPipeline(object):
	def __init__(self):
		self.settings = get_project_settings()
		self.urlUtilsObj = UrlUtils()

	def process_item(self, item, spider):
		response = item['response']
		if (self.urlUtilsObj.getPageType(response.url) == self.settings.get('CATEGORY_PAGE_TYPE')):
			self.timeStamp = item['timeStamp']
			return self.parseCategoryResponse(response)
		else:
			return item
	
	def parseCategoryResponse(self, response):
		catItem = AECategoryItem()
		catItem['url'] = self.urlUtilsObj.trimUrlParams(response.url)
		catItem['catId'] = self.urlUtilsObj.getIdFromUrl(response.url)
		catItem['size'] = int(len(response.body))
		catItem['timeStamp'] = self.timeStamp
		catItem['responseCode'] = response.status
		print (catItem)

