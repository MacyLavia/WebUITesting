from FinalAssignment.pageobject.index_page import IndexPage

class TestIndex_checklist():
    def test_checklist(self, login):
        # 使用conftest中的全局驱动login
        driver = login
        checklist_page_obj = IndexPage(driver)
        checklist_text = checklist_page_obj.goto_checklist()
        assert checklist_text == '热搜榜'

