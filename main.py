import os
import sys

# Import Qt GUI component
import threading

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog
from PyQt5.uic.properties import QtWidgets

from core.core import Configuration
from core.mysign import MySignals
from core.zipextract import PwdParser

# dirname = os.path.dirname(PySide6.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# Self Function
# from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from ui.zipmain import Ui_ZipMainWindow


class ZipMainWindow(QMainWindow, Ui_ZipMainWindow):
    my_sign = None

    def __init__(self, parent=None):
        super(ZipMainWindow, self).__init__(parent)
        self.my_sign = MySignals()
        self.setupUi(self)
        # Connect button click event to PrintHello function
        self.control_button_start_pause.clicked.connect(self.start_parse_password)
        self.my_sign.sign_zip_label_digital.connect(self.set_zip_label_digital)
        self.my_sign.sign_correct_passwrod.connect(self.set_success_password)
        self.setting_button_fileopen.clicked.connect(self.open_zip_file_dialog)

    def start_parse_password(self):
        filename = self.setting_input_file.text()
        if filename is None or len(filename) == 0:
            QMessageBox.critical(self, "告警", "请选择解压文件!", QMessageBox.Yes)
            return

        config = Configuration()
        config.thread_num = int(self.setting_input_thread_num.text())
        config.zip_file = filename
        # t = threading.Thread(target=do_main, args=(self.my_sign, config))
        pwd = PwdParser(self.my_sign, config)
        pwd.start()

    def set_zip_label_digital(self, now, total):
        self.progress_text_pregress_digital.setText(f"{now} / {total}")
        self.progress_pregress_bar.setValue(now / total * 100)

    def set_success_password(self, pwd):
        self.progress_input_result.setText("成功！ 密码为：" + pwd)

    def set_failure_result(self):
        self.progress_input_result.setText("失败！ 没有找到密码")

    def open_zip_file_dialog(self):
        directory = QFileDialog.getOpenFileName(self, "getOpenFileName", "./",
                                                          "Rar Files (*.rar);Zip Files (*.zip)")
        self.setting_input_file.setText(directory[0])


Program = QApplication(sys.argv)
Window = ZipMainWindow()

if __name__ == '__main__':
    Window.show()
    Program.exec_()
