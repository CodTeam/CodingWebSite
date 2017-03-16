# coding=utf-8
from es_services.es_service_base import ESBase

class ESSuggestService(ESBase):

    def suggest(self,query,tag="tags", suggest_size=10):
        es_suggest_options = self.set_suggest_optional(query, tag, suggest_size)

        es_result = self.es.suggest(index=self.es_index, body=es_suggest_options)
        final_results = self.get_suggest_list(es_result)
        return final_results

    def get_suggest_list(self,es_result):
        result_items = es_result['suggest'][0]["options"]
        final_results = []
        for item in result_items:
            final_results.append(item['text'])
        return final_results

    def set_suggest_optional(self,query, tag, suggest_size):
        es_suggest_options = {
            "suggest": {
                "text": query,
                "completion": {
                    "field": tag,
                    "size": suggest_size
                }
            }
        }
        return es_suggest_options