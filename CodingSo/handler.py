# coding=utf-8
import tornado.ioloop
from tornado.options import options
from tornado.web import url
import templates
import api_search
import api_suggest
import api
import sys
import platform

if platform.system() == 'Linux':
    static_file_path = '/data/app/CodingSo/static'
else:
    static_file_path = r'C:\workspace\mixpanel\static'

if __name__ == '__main__':
    settings = {
        "template_path": "templates",
        "static_path": "static",
        "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        "login_url": "/signin",
        "xsrf_cookies": False,
    }
    app = tornado.web.Application(
        debug=True,
        handlers=[
            url(r"/static/(.*)",
                api.NoCacheStaticFileHandler, {
                    "path": static_file_path
                }, name="static"),
            (r"/", templates.HomePageTemplate),
            (r"/s", templates.SearchResultTemplate),
            (r"/json", templates.JsonEditorToolTemplate),
            (r"/v1/search", api_search.SearchHanlderV1),
            (r"/v1/suggest", api_suggest.SuggestRelatedKeywordHandlerV1)

        ], **settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    #     http_server.listen(options.port)
    if len(sys.argv) > 1:
        http_server.bind(sys.argv[1])
    else:
        http_server.bind(options.port)
    http_server.start(1)
    tornado.ioloop.IOLoop.instance().start()
