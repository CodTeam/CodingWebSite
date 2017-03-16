# coding=utf-8
from basehandler import BaseHandler

class HomePageTemplate(BaseHandler):
    def get(self):
        self.render('main/index.html')


class SearchResultTemplate(BaseHandler):
    def get(self):
        self.render('main/searchResult.html')


class JsonEditorToolTemplate(BaseHandler):
    def get(self):
        self.render('main/json_editor.html')