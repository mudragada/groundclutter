# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from pyes import ES

# class ElasticSearchPipeline(object):
# 	def __init_(self):
# 		self.settings = get_project_settings()
# 		uri = "{}:{}".format(self.settings['ELASTISEARCH_SERVERS'], self.settings['ELASTICSEARCH_PORT'])
# 		print("############" + str(uri))
# 		self.es = ES([uri])
# 	def process_item(self, item, spider):
# 		index_name = 'ae_cat'
# 		print(" ################# IN PROCESS_ITEM ###########")
# 		self.es.index(dict(item), index_name, 'items', op_type='create')
# 		return item

# class AecrawlerPipeline(object):
#     def process_item(self, item, spider):
#         return item
