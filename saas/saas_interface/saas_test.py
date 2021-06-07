# encoding: utf-8
# @Time    : 2021/6/7 2:33 下午
# @Author  : Sail
# @File    : saas_test.py
# @Software: PyCharm
import allure
import pytest
import requests

from common.httpclient import MyHttpClient
from common.read_yaml import ReadYaml

date=ReadYaml().getYaml()
print(date["list_date"])
@allure.feature("测试yapi首页接口")

class TestSaasInf():
    @pytest.fixture(scope="class")
    def login(self):
        """
        登录， 返回session， 末尾登出
        :return:
        """
        url="http://666.xxx.cn/api/user/login"
        date={"email": "xxx.999@000.com", "password": "777"}
        headers={
            "User_Agent":"Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045329 Mobile Safari/537.36 MMWEBID/4678 MicroMessenger/7.0.18.1740(0x27001239) Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64"
        }
        s=requests.Session()
        r=s.post(url, data=date, headers=headers)
        yield s
        r = s.get("http://0000.0000.cn/api/user/logout")

    @allure.step("项目列表")
    def test_group(self,login):
        """
        测试yapi项目列表
        :param login:
        :return:
        """
        url="http://0000.0000.cn/api/group/get_mygroup"
        res=login.get(url).json()

        assert res.get("errmsg")=="成功！"

    @allure.step("接口列表")
    @pytest.mark.parametrize("url,group_id,page,limit", date["list_date"],
                             ids=["分页第一页",
                                  "分页第二页",
                                  ])
    def test_list(self,login,url,page,limit,group_id):
        """
        测试分组
        """
        dict={
            "group_id":int(group_id),
            "page":page,
            "limit":limit
        }
        res=login.get(url=url,params=dict).json()
        assert res.get("errmsg")=="请求参数 data.group_id 应当是 number 类型"




