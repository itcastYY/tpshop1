# -*- coding=utf-8 -*-
from page.page_home import HomePageAction
from page.page_myself import MyselfPageAction


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def inithomepage(self):
        return HomePageAction(self.driver)

    @property
    def initmyselfpage(self):
        return MyselfPageAction(self.driver)