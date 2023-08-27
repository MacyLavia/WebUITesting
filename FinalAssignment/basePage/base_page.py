import time

from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FinalAssignment.base_tools.my_logger import logger
import traceback

def init_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

class BasePage():
    """
    初始化基本页面对象
    """
    # 会默认调用init方法
    def __init__(self, driver):
        # 实例化浏览器对象,不会这样重新创建，而是直接传一个driver
        self.driver = driver
        logger.info("设置浏览器最大化")
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(10)

    def my_get_url(self, url):
        """
        获取指定url页面
        :return:
        """
        logger.info("打开url：{}".format(url))
        self.driver.get(url)

    def my_find_element(self, ele, time_out=10):
        """
        封装查找元素的方法
        :param ele:传入的元素是元组的类型，例如：（‘id’, 'kw'）
        :return:
        """
        # self.element = self.driver.find_element(ele)
        logger.info("查找元素：{}，超时时间：{}".format(ele, time_out))
        try:
            self.element = WebDriverWait(self.driver, time_out, 0.5).until(EC.presence_of_element_located(ele))
        except:
            logger.warning("元素定位失败，请检查，报错信息如下：", traceback.print_exc())
            raise Exception("元素定位失败")
        # sleep(3)

    def my_click(self, ele, time_out=10):
        """
        封装点击元素的方法
        :return:
        """
        # 查找元素
        self.my_find_element(ele, time_out)
        # 点击元素
        self.element.click()

    def my_send_keys(self, ele, send_word):
        """
        封装元素内输入内容
        :return:
        """
        # 查找元素
        self.my_find_element(ele)
        self.element.send_keys(send_word)

    def get_cookies(self):
        """
        获取cookies
        :return:
        """
        self.cookies = self.driver.get_cookies()
        print(self.cookies)

    def set_cookies(self, cookies):
        """
        设置cookies的方法
        :return:
        """
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def my_refresh(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def get_element_text(self, ele):
        """
        获取元素文本值
        :return:
        """
        self.my_find_element(ele)
        return self.element.text

    def get_element_title(self, ele):
        """
        获取元素title值
        :param ele:
        :return:
        """
        self.my_find_element(ele)
        # self.element.get_attribute("title")
        return self.element.get_attribute("title")

    def get_element_placeholder(self, ele):
        """
        获取元素placeholder值
        :param ele:
        :return:
        """
        self.my_find_element(ele)
        return self.element.get_attribute("placeholder")

    def my_quit(self):
        self.driver.quit()

# 测试能否正常运行
# 获取cookies
# 初始化页面对象
# index_page = BasePage()
# index_page.my_get_url("https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F")
# time.sleep(10)
# # # 点击登录按钮
# # index_page.my_click()
# # 获取cookies
# index_page.get_cookies()
# # 打印cookies信息
# print(index_page.cookies)

from 实验四_0602.config import *

# driver = webdriver.Chrome(ChromeDriverManager().install())
# index_page = BasePage(driver)
# index_page.my_get_url(index_url)
# index_page.set_cookies(cookies)
# index_page.my_refresh()
# time.sleep(5)
# index_page.my_quit()


