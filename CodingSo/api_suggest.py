# coding=utf-8
from basehandler import BaseHandler
from es_services.es_suggest_service import ESSuggestService

es_sugg_service = ESSuggestService()


class SuggestRelatedKeywordHandlerV1(BaseHandler):
    def get(self):
        ret = {"ret": "0", "msg": "", "data": ""}
        if self.get_arguments("kw") is None:
            self.write(ret)
            self.finish()
            return

        try:
            ret["data"] = es_sugg_service.suggest(self.get_arguments("kw")[0], "tags", 5)
            print(ret)
            self.write(ret)
        except Exception as ex:
            print(ex)
            ret["ret"] = "1"
            self.write(ret)
            self.finish()
