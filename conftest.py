# encoding: utf-8
# @Time    : 2021/6/1 5:50 下午
# @Author  : Sail
# @File    : conftest.py.py
# @Software: PyCharm
import pytest
from selenium import webdriver


def pytest_emoji_passed(config):
    return u'✅ ', u'PASSED ☑️ '


def pytest_emoji_failed(config):
    return u'👎 ', u'FAILED 👎 '


def pytest_emoji_skipped(config):
    return u'🏃 ', u'SKIPPED 🏃 '


def pytest_emoji_error(config):
    return u'❎ ', u'ERROR ❌ '


def pytest_emoji_xfailed(config):
    return u'🤓 ', u'xfail 🤓 '


def pytest_emoji_xpassed(config):
    return u'😜 ', u'XPASS 😜 '



@pytest.fixture(scope="session")
def init_driver():
    chrome_driver_path = "/Users/sail/util/chrome_driver/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    return driver
