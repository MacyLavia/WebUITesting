from FinalAssignment.pageobject.index_page import IndexPage


class TestIndex_search():
    def test_search_weibo(self, login):
        driver = login
        search_weibo_page = IndexPage(driver)
        search = search_weibo_page.goto_search()
        assert search == "搜索微博"

