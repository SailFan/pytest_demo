# encoding: utf-8
# @Time    : 2021/6/3 6:48 下午
# @Author  : Sail
# @File    : test_login.py
# @Software: PyCharm
import time

import allure
import pytest
from common.read_yaml import ReadYaml
from saas.saas_page.login_page.loginPage import LoginPage

date=ReadYaml().getYaml()
print(date["account"])
@allure.feature("测试登录接口")
class TestLogin():
    """
    测试登录相关的页面
    """
    @pytest.fixture(scope="class")
    def up_down(self,init_driver):
        login = LoginPage(init_driver)
        login.get("https://kashangbao-test.360che.com/index.html#/login")
        yield login
        login.w.quit()


    @pytest.mark.parametrize("username,password,expect", date["account"],
                             ids=["正常登录",
                                  "密码为空登录",
                                  "账号为空登录",
                                  ])
    @allure.step('账号，密码登录')
    @pytest.mark.run(order=1)
    def test_login(self,username,password,expect,up_down):
        """
            这个方法用来测试登录
        """
        up_down.account=1
        assert 1==1
    @allure.step('首页跳转其他页面测试')
    @pytest.mark.run(order=2)
    def test_home_skip(self):
        print("zhixing")
        assert 1==3

    @pytest.mark.flaky(reruns=3,reruns_delay=1)
    def test_fail(self):
        raise RuntimeError("我抛出了一个错误")


