# -*- coding=utf-8 -*-
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
        self.click( self.enter_btn_feature )


