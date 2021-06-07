# encoding: utf-8
# @Time    : 2021/5/23 11:15 下午
# @Author  : Sail
# @File    : main.py
# @Software: PyCharm
import os

import pytest


if __name__ == '__main__':
    pytest.main()

    os.system("allure generate ./report/result_allure -o ./report/result_html -c")

