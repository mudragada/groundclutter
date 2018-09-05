# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import datetime, time

class WebHttpResponse(Item):
	response = Field()
	timeStamp = Field()
	startUrl = Field()

class WebCategoryItem(Item):
	timeStamp = Field()
	responseCode = Field()
	url = Field()
	catId = Field()
	size = Field()
	pics = Field()

class WebProductItem(Item):
	timeStamp = Field()
	responseCode = Field()
	size = Field()
	url = Field()
	productId = Field()
	productName = Field() ## div class="psp-product-txt".## h1 class="psp-product-name"
	productAvailability = Field() ## div class="psp-product-availability"
	listPrice = Field() ## div class="psp-product-price".## s. ##span class="psp-product-listprice"
	salePrice = Field() ## div class="psp-product-price".## s. ##span class="psp-product-saleprice".text
	pspDiscountText = Field() ##div class="psp-product-price".## span class="psp-product-yousave".text
	pspPromoText = Field() ##div class="psp-product-promo".## span
	skus = Field() ##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li[] class="size-option".data-sku.text
	styleWith = Field()  ##div id ="pdp-bundle-section". ## div class="product-list". ## div[].id
	recommendedProds = Field() ## div id=awo_rms
	picsUrls = Field() ## div id = "product-carousel" class="pdp-carousel"

class WebSkuItem(Item):
	skuId = Field() ##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li class="size-option".data-sku.text
	sizeName = Field()##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li class="size-option".a.text
	inventory = Field() ##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li class="size-option".data-outofstock.text
	outOfStock = Field() ##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li class="size-option".data-stock.text
	onlineOnly = Field() ##div class="ddropdown-selection". ## ul id="psp-sizedropdown-menu".#li class="size-option".data-onlineonly.text

class WebPicsItem(Item):
	url = Field()
	size = Field()
	
