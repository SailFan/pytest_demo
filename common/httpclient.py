# encoding: utf-8
# @Time    : 2021/6/7 2:06 下午
# @Author  : Sail
# @File    : httpclient.py
# @Software: PyCharm

import requests
from requests.adapters import HTTPAdapter


class MyHttpClient:
    def __init__(self, timeout=8):
        """
        :param timeout: 每个请求的超时时间
        """
        s = requests.Session()
        ##: 在session实例上挂载Adapter实例, 目的: 请求异常时,自动重试
        s.mount('http://', HTTPAdapter(max_retries=3))
        s.mount('https://', HTTPAdapter(max_retries=3))

        ##: 设置为False, 主要是HTTPS时会报错, 为了安全也可以设置为True
        s.verify = False

        ##: 公共的请求头设置

        ##: 挂载到self上面
        self.s = s
        self.timeout = timeout

    def get(self, url, query_dict):
        """GET

        :param url:
        :param query_dict: 一般GET的参数都是放在URL查询参数里面
        :return:
        """

        return self.s.get(url, params=query_dict)

    def post(self, url, form_data=None, body_dict=None):
        """POST

        :param url:
        :param form_data: 有时候POST的参数是放在表单参数中
        :param body_dict: 有时候POST的参数是放在请求体中(这时候 Content-Type: application/json )
        :return:
        """
        if form_data:
            return self.s.post(url, data=form_data)
        if body_dict:
            return self.post(url, json=body_dict)

    def __del__(self):
        """当实例被销毁时,释放掉session所持有的连接

        :return:
        """
        if self.s:
            self.s.close()