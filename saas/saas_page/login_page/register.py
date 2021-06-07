# encoding: utf-8
# @Time    : 2021/6/5 11:42 下午
# @Author  : Sail
# @File    : register.py
# @Software: PyCharm
from page_objects import PageObject, PageElement


class RegisterPage(PageObject):
    """
        saas 注册页面
    """
    contacts = PageElement(css="input[placeholder='请填写全名，方便我们与您联系']")
    contacts = PageElement(css="input[placeholder='本号码将应用于接收用户名和密码、账号登录']")
    contacts = PageElement(css="input[placeholder='请填写短信验证码']")
    contacts = PageElement(css=".get-code")
    contacts = PageElement(tag_name="button")
