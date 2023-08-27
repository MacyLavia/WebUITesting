from FinalAssignment.pageobject.index_page import IndexPage


class TestIndex_send():
    def test_send_weibo(self, login):
        # 使用conftest中的全局驱动login
        driver = login
        send_weibo_page = IndexPage(driver)
        send = send_weibo_page.goto_send()
        assert send == "仅自己可见"

