## URL Utils
import re
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector


class UrlUtils(object):
  def __init__(self):
    self.settings = get_project_settings()
  def getIdFromUrl(self, url):
    if("s-cat" in url or "s-cms" in url or "s-cms" in url or "s-prod" in url):
      idRegex = re.compile(self.settings.get('REGEX_CATALOG_URL'))
      return str(idRegex.search(url).group('id'))
    else:
      return ""

  def trimUrlParams(self, unTrimmed):
    if(unTrimmed):
      urlRegex = re.compile("(?P<trimmedUrl>.*?)(?=\?)")
      matchList = re.findall(urlRegex, unTrimmed)
      if(len(matchList) !=0 and type(matchList) != 'NoneType'):
        return matchList[0]
  
  def getXPathStr(self, response, xpathConfig):
    responseSelector = Selector(response)
    return str(responseSelector.xpath(self.settings.get(xpathConfig)).extract_first())

  def getPageType(self, targetUrl):
    if(targetUrl != None and any(substring in targetUrl for substring in self.settings.get('CATEGORY_URL_IDENTIFIER'))):
      return self.settings.get('CATEGORY_PAGE_TYPE')
    elif(targetUrl != None and any(substring in targetUrl for substring in self.settings.get('PRODUCT_URL_IDENTIFIER'))):
      return self.settings.get('PRODUCT_PAGE_TYPE')
    else:
      return ""