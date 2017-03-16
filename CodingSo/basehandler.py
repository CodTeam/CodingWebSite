#coding=utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import platform
from tornado.options import define, options

if platform.system() == 'Darwin':
    define("port", default=8000, help="", type=int)
elif platform.system() == 'Linux':
    define("port", default=8091, help="", type=int)
else:
    define("port", default=80, help="", type=int)
tornado.options.parse_command_line()

class BaseHandler(tornado.web.RequestHandler):



    def get_template_namespace(self):
        namespace = dict(
            handler=self,
            request=self.request,
            current_user=self.current_user,
            locale=self.locale,
            _=self.locale.translate,
            pgettext=self.locale.pgettext,
            static_url=self.static_url,
            xsrf_form_html=self.xsrf_form_html,
            reverse_url=self.reverse_url,
        )
        namespace.update(self.ui)
        return namespace








