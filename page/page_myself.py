# -*- coding=utf-8 -*-
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.baseaction import Baseaction


# 下面这个类里面存放所有 我的 界面模型测试时需要使用的动作
class MyselfPageAction(Baseaction):

    # 将 myself 界面中会用到的元素特征都准备好
    login_reg_feature = By.XPATH,"text,登录/注册,1"
    num_input_feature = By.ID,"com.tpshop.malls:id/edit_phone_num"
    pwd_input_feature = By.ID,"com.tpshop.malls:id/edit_password"
    enter_btn_feature = By.ID,"com.tpshop.malls:id/btn_login"
    set_btn_feature = By.ID,"com.tpshop.malls:id/setting_btn"
    out_btn_feature = By.ID,"com.tpshop.malls:id/exit_btn"

    # 点击 登录/注册  的动作
    def click_login_reg(self):
        self.click(self.login_reg_feature)

    # 在账号框中转入账号的动作
    def input_num(self,value):
        self.input_txt(self.num_input_feature,value)

    # 在密码框中输入 密码 的动作
    def input_pwd(self,value):
        self.input_txt(self.pwd_input_feature,value)

    # 点击登录的 动作
    def click_enter(self):
        # 我们打开图片所有的地方，然后将图片里的信息以二进制的形式读取出来，存放在 imgFile中
        imgFile = open( "./img/01.png","rb" ).read()
        allure.attach("这是截图",imgFile,allure.attach_type.PNG)
        self.click( self.enter_btn_feature )

    # 定义一个动作它可以返回一个布尔值用来判断当前用户是否登录，如果登录则返回True
    def is_loging(self):
        # 去查找 登录/注册按钮，如果找不到则证明登录，那么我们就返回 True
        try:
            self.find_element( self.login_reg_feature )
            return False
        except Exception:
            return True

    # 定义一个函数，用来实现账号的退出操作
    def login_out(self):
        self.click( self.set_btn_feature )
        time.sleep( 2 )
        self.click( self.out_btn_feature )




























