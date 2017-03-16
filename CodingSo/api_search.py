# coding=utf-8
from basehandler import BaseHandler
from es_services.es_search_service import ESSearchService
import json
es_service = ESSearchService()

class SearchHanlderV1(BaseHandler):

    def post(self):
        ret={"ret":"0","msg":"","data":"","total_count":0}
        try:
            if self.get_argument("kw") is None or self.get_argument("from") is None or self.get_argument("pagenum") is None:
                self.redirect("/")
                self.finish()
            else:
                kw = self.get_argument("kw")
                from_count = self.get_argument("from")
                page_size = self.get_argument("pagenum")
                # total_re = es_service.get_total_count(kw)
                # if total_re is None or total_re.get("count") ==0:
                #     ret["total_count"] =0
                #     self.write(ret)
                #     self.finish()
                #     return
                # else:
                #     ret["total_count"] = total_re.get("count")
                #     result = es_service.search_keyword(kw)
                #     ret["data"] = result.get("hits")
                #     # print(result)
                #     self.write(ret)
                result = es_service.search_keyword(kw,from_count,page_size)

                ret["total_count"] = result.get("hits").get("total")
                #     result = es_service.search_keyword(kw)
                ret["data"] = result.get("hits")
                #     # print(result)
                self.write(ret)
        except Exception as ex:
            ret["ret"] = "1"


