import pytest
import os
from FinalAssignment.base_tools.my_logger import logger

if __name__ == '__main__':
    logger.info("开始执行UI自动化测试用例".format(50, "*"))
    pytest.main()
    logger.info("UI自动化测试用例执行完成".format(50, "*"))
    os.system(r"allure generate .\report\report_json\ -o .\report\html --clean")

