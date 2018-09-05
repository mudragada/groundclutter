# -*- coding: utf-8 -*-

# Scrapy settings for AECrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WebCrawler'

SPIDER_MODULES = ['AECrawler.spiders']
NEWSPIDER_MODULE = 'AECrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'AECrawler'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_magicfields.MagicFieldsMiddleware': 100
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'AECrawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
'AECrawler.pipelines.category.CategoryInfoPipeline' : 1,
'AECrawler.pipelines.product.ProductInfoPipeline' : 2,
}
ELASTICSEARCH_SERVER = 'http://localhost:9200'
ELASTICSEARCH_INDEX = 'ae_pagedata'
ELASTICSEARCH_TYPE = 'page'
ELASTICSEARCH_TIMEOUT = 60
ELASTICSEARCH_BUFFER_LENGTH = 9999
#ELASTICSEARCH_UNIQ_KEY = 'url'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 5
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_LEVEL = 'INFO'

############################################## CUSTOM SETTINGS ################################################

REGEX_CATALOG_URL = '\/(s\-(?:prod|cat|mm|cms))\/(?P<id>.*?)(?:\s+|\?|\&|$)'
CATEGORY_URL_IDENTIFIER = ['s-cat', 's-mm', 's-cms']
PRODUCT_URL_IDENTIFIER = ['s-prod']
CATEGORY_PAGE_TYPE = "category"
PRODUCT_PAGE_TYPE = "product"
XPATH_TOPNAV_URL = '/html/body//*/div[contains(@class, "top-link-container")]//a'
XPATH_CAT_URL = '/html/body//*/a[contains(@href, "s-cat") or contains(@href, "s-cms") or contains(@href, "s-mm")]'
XPATH_PROD_URL = '/html/body//*/a[contains(@href, "s-prod")]'

## AEProductItem
XPATH_PRODUCT_PAGE_NAME = '/html/body//*/h1[contains(@class, "psp-product-name")]/text()'
XPATH_PRODUCT_PAGE_AVAILABILITY = '/html/body//*/div[contains(@class, "psp-product-availability")]/span/text()'
XPATH_PRODUCT_PAGE_LIST_PRICE = '/html/body//*/span[contains(@id, "psp-regular-price")]/text()'
XPATH_PRODUCT_PAGE_SALE_PRICE = '/html/body//*/span[contains(@id, "psp-sale-price")]/text()'
XPATH_PRODUCT_PAGE_DISCOUNT_TEXT = '/html/body//*/span[contains(@class, "psp-product-yousave")]/text()'
XPATH_PRODUCT_PAGE_PROMO_TEXT = '/html/body//*/div[contains(@class, "psp-product-promo")]/span/text()'

