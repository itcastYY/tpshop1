# -*- coding=utf-8 -*-
import time
from base import initDriver
from page.page import Page


class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 定义一个 test 函数来对应我们测试用例中执行结果为 “账号不存在” 的那一类用例
    def test_login_nonum(self):

        # 使用 首页模型当中的进入 首页的动作
        self.page.inithomepage.auto_enter_home()
        self.page.inithomepage.click_myself()
        time.sleep(2)  # 涉及到页面转场我们选择停留一定的时间

        # 点击登录注册按钮
        self.page.initmyselfpage.click_login_reg()
        time.sleep(1)  # 涉及到页面转场我们选择停留一定的时间

        # 输入账号
        self.page.initmyselfpage.input_num("18513891234")

        # 输入密码
        self.page.initmyselfpage.input_pwd("123456")

        # 点击登录
        self.page.initmyselfpage.click_enter()

        # 测试登录点击之后的 toast 获取
        toast_neirong = self.page.initmyselfpage.get_toast_content("账号不存")
        # 添加断言
        assert toast_neirong == "账号不存在!"


