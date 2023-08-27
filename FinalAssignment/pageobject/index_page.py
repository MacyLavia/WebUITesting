import time
from FinalAssignment.basePage.base_page import BasePage
from selenium.webdriver.common.by import By
from FinalAssignment.config import *
from time import sleep
from selenium.webdriver.common.keys import Keys

class IndexPage(BasePage):
    # 因为init方法和BasePage的init方法一样，所以可以不写
    def goto_login(self):
        self.my_get_url(index_url)
        title = self.get_element_title(ele=(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div/div/div/a[5]/div'))
        print(title)
        return title

    def goto_send(self):
        self.my_get_url(index_url)
        # 点击编辑框，输入“测试微博发送微博功能”
        self.my_send_keys(ele=(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[1]/div/textarea'),send_word="测试微博发送微博功能")
        sleep(3)
        # 修改权限为”仅自己可见“
        self.my_click(ele=(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[3]/span/div/div[1]'))
        self.my_click(ele=(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[3]/div/div/div[4]'))
        # 点击【发送】按钮
        self.my_click(ele=(By.XPATH, '//*[@id="homeWrap"]/div[1]/div/div[4]/div/div[4]/button'))
        sleep(3)
        send = self.get_element_text(ele=(By.XPATH, '//*[@id="scroller"]/div[1]/div[1]/div/article/div[1]/div/div[1]/span'))
        print(send)
        return send

    def goto_search(self):
        # 搜索框搜索“高考结束了”
        self.my_send_keys(ele=(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/span/form/div/input'), send_word="高考结束了")
        sleep(3)
        # 回车实现点击搜索
        self.my_send_keys(ele=(By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div/span/form/div/input'), send_word=Keys.ENTER)
        sleep(3)
        # 获取所有窗口的句柄
        handle1 = self.driver.window_handles
        # 切换句柄
        self.driver.switch_to.window(handle1[-1])
        # 获取“搜索微博”内容
        search = self.get_element_placeholder(ele=(By.XPATH, '//*[@id="searchapps"]/div/div[1]/div/div/div[1]/div/div[2]/div/span/form/div/input'))
        return search

    def goto_newgroup(self):
        # 点击自定义分组的【管理】按钮
        self.my_click(ele=(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div/div/div/div[2]/div/button'))
        # div弹窗获取”管理自定义分组“文本
        text = self.get_element_text(ele=(By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[1]/div/div[1]'))
        print(text)
        # 进行断言
        assert text == '管理自定义分组'
        # 点击新建分组
        self.my_click(ele=(By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div/div[2]/div[4]/button'))
        time.sleep(3)
        # 新建“测测”分组
        self.my_send_keys(ele=(By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div/div[2]/input'),send_word="测测")
        time.sleep(3)
        # 点击确定按钮
        self.my_click(ele=(By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[3]/button[2]'))
        time.sleep(3)
        # 删除新建分组
        self.my_click((By.XPATH, '//div[text()=" 测测 "]/following-sibling::i'))
        time.sleep(3)
        # 点击确定删除“测测”分组
        self.my_click(ele=(By.XPATH, '//*[@id="app"]/div[5]/div[1]/div/div[2]/button[2]'))
        time.sleep(3)
        # 关闭管理窗口
        self.my_click(ele=(By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[1]/div/div[2]/i'))
        time.sleep(3)

    def goto_checklist(self):
        self.my_get_url(index_url)
        # 点击【查看完整热搜榜单】
        self.my_click(ele=(By.XPATH, '//*[@id="__sidebar"]/div/div[2]/div/div[1]/div/div/div[3]/a/div/div'))
        sleep(3)
        # 获取“热搜榜”文字
        checklist_text = self.get_element_text(ele=(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div/div/div/a[4]/div/span'))
        print(checklist_text)
        return checklist_text

# driver = webdriver.Chrome(ChromeDriverManager().install())
# index_page = IndexPage(driver)
# index_page.my_get_url("https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F")
# sleep(10)
# # 获取cookies
# # index_page.get_cookies()
# # 登录
# index_page.goto_login()
# # 设置cookie，绕过登录
# # index_page.my_click(ele=(By.XPATH, '//*[@id="__sidebar"]/div/div[2]/div[1]/div/button'))
# # index_page.set_cookies(cookies)
# # index_page.my_refresh()
# # 发微博
# # index_page.send_weibo()
# sleep(2)
# # 搜索
# index_page.goto_search()
# sleep(5)
#
# index_page.my_quit()
