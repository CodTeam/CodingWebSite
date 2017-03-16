# coding=utf-8
from es_services.es_service_base import ESBase


class ESSearchService(ESBase):
    # self.es.cluster.health(wait_for_status='yellow', request_timeout=120)
    # print(self.es.info())

    def search_keyword(self, keyword,from_count,page_size):
        # return self.es.search(index=self.es_index, body={"query":{"match":{"content":keyword}}})
        return self.es.search(index=self.es_index, body={"from":from_count,"size":page_size,
            "query": {"multi_match": {"query": keyword, "fields": ["title", "tags", "keywords", "desc", "content"]}},
        "highlight":{"fields":{"desc":{"pre_tags":["<b>"],"post_tags":["</b>"]}}}})

    def get_total_count(self, keyword):
        return self.es.count(index=self.es_index, body={
            "query": {"multi_match": {"query": keyword, "fields": ["title", "tags", "keywords", "desc", "content"]},"term":{"title":keyword}},
        "highlight":{"fields":{"desc":{"pre_tags":["<b>"],"post_tags":["</b>"]}}}})
