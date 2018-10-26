# -*- coding=utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base import initDriver
from page.page import Page
import pytest
pytestmark = pytest.mark.skip( "跳过首页测试" )

class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_demo(self):
        # 先进入主界面
        self.page.inithomepage.auto_enter_home()
        time.sleep( 2 )

        # 点击手机的返回键
        self.driver.press_keycode(4)

        # 想办法去获取 toast
        wait = WebDriverWait( self.driver,5,0.1 )
        ele = wait.until(lambda x:x.find_element(By.XPATH, "//*[contains(@text,'再按一次退')]"))
        print( ">>>>>>>>>>>",ele.text )



