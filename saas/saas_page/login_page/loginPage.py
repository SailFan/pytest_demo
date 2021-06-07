# encoding: utf-8
# @Time    : 2021/6/3 1:54 下午
# @Author  : Sail
# @File    : loginPage.py
# @Software: PyCharm

import os
from datetime import datetime

from page_objects import PageObject, PageElement
from selenium import webdriver

class LoginPage(PageObject):

    """
        saas 系统登录页面
    """
    account = PageElement(css="input[placeholder='请输入帐号/手机号']")
    password = PageElement(css="input[placeholder='请输入密码']")
    verification = PageElement(css="input[placeholder='请输入验证码']")
    register = PageElement(css="p.regist span")
    rememberMe=PageElement(xpath="/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/label/span")
    forget=PageElement(css=".regist span[class='forgetPsw']")
    cut=PageElement(tag_name="em")
    loginBtu=PageElement(tag_name="button")
    home=PageElement(partial_link_text="首页")
    joinUs=PageElement(partial_link_text="加入我们")

    def sava_png(self):
        filename = datetime.now().strftime("%Y:%m:%d:%H:%M:%S") + self.w.title + ".png"
        father_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "../../../")
        img_path="report/img"
        self.w.save_screenshot(os.path.join(father_path, img_path,filename))




