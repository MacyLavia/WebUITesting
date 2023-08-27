from FinalAssignment.pageobject.index_page import IndexPage


class TestIndex_login():
    def test_login(self, login):
        # 使用conftest中的全局驱动login
        driver = login
        login_page_obj = IndexPage(driver)
        title = login_page_obj.goto_login()
        assert title == "名人明星"




