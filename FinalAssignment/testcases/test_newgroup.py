from FinalAssignment.pageobject.index_page import IndexPage


class TestIndex_newgroup():
    def test_newgroup(self, login):
        # 使用conftest中的全局驱动login
        driver = login
        newgroup_page_obj = IndexPage(driver)
        newgroup_page_obj.goto_newgroup()



