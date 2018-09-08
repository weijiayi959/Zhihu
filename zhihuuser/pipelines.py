# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class ZhihuuserPipeline(object):
    # 用来保存到mongodb数据库
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri  # 连接MongoDB
        self.mongo_db = mongo_db  # 项目文件

        # 从全局配置settings里拿到MONGO数据库的配置信息

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

        # 在进行spider前的初始化操作

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)  # 连接数据库
        self.db = self.client[self.mongo_db]  # 创建项目

    def process_item(self, item, spider):
        name = self.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
