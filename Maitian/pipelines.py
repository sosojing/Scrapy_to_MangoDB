# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.utils.project import get_project_settings

class MaitianPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_DOCNAME']]

    # 数据持久化
    def process_item(self, item, spider):
        zufang = dict(item)
        self.post.insert(zufang)
        return item
