import logging
import os
import time

class Logger():

    def __init__(self):
        # 初始化记录器
        self.logger = logging.getLogger()
        # 设置记录器的日志等级
        self.logger.setLevel(logging.INFO)

        # 控制台输出的处理器
        sh = logging.StreamHandler()
        # 设置日志等级
        sh.setLevel(logging.INFO)

        # 处理日志文件路径
        # 文件名配置
        file_name = "{}.log".format(time.strftime("%Y-%m-%d"))
        file_path = os.path.join(os.path.dirname(__file__), '..', "log")
        if not os.path.isdir(file_path):
            os.makedirs(file_path)

        # 文件输出的处理器
        fh = logging.FileHandler(filename=os.path.join(file_path, file_name), encoding="utf-8")
        # 设置日志等级
        fh.setLevel(logging.INFO)

        # 定义日志输出格式
        formatter = logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s|%(lineno)s|%(message)s")
        # 设置处理器中日志输入格式
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        # 处理器添加到记录器中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

logger = Logger().logger

