# coding=utf-8
from elasticsearch import Elasticsearch
class ESBase(object):
    def __init__(self):
        self.es = Elasticsearch([{'host': '103.248.223.134', 'port': 9200}])
        self.es_index = "codingso"