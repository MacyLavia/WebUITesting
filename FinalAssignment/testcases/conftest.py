import time
import pytest
from FinalAssignment.basePage.base_page import BasePage
from FinalAssignment.config import *
from FinalAssignment.basePage.base_page import init_driver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def login():
    driver = init_driver()
    # 登录，初始化页面对象
    page_obj = BasePage(driver)
    # 打开新浪微博首页
    page_obj.my_get_url(index_url)
    # 点击登录按钮
    page_obj.my_click(ele=(By.XPATH, '//*[@id="__sidebar"]/div/div[2]/div[1]/div/button'))
    # 设置cookies绕过登录
    page_obj.set_cookies(cookies)
    page_obj.my_refresh()
    time.sleep(3)
    # return page_obj.driver
    yield page_obj.driver
    # 退出页面
    page_obj.my_quit()
