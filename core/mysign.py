from threading import Thread

from PyQt5.QtCore import QObject, pyqtSignal


# class Signal(object):
#     pass


class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    sign_zip_process_bar = pyqtSignal(int, int)
    # 还可以定义其他信号
    sign_zip_label_digital = pyqtSignal(int, int)
    sign_correct_passwrod = pyqtSignal(str)
    sign_log = pyqtSignal(str)
