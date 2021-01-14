from threading import Thread

from PySide6.QtCore import QObject, Signal


class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    sign_zip_process_bar = Signal(int, int)
    # 还可以定义其他信号
    sign_zip_label_digital = Signal(int, int)
    sign_correct_passwrod = Signal(str)
