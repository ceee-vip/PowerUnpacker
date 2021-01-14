# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zipmain.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ZipMainWindow(object):
    def setupUi(self, ZipMainWindow):
        if not ZipMainWindow.objectName():
            ZipMainWindow.setObjectName(u"ZipMainWindow")
        ZipMainWindow.setWindowModality(Qt.ApplicationModal)
        ZipMainWindow.setEnabled(True)
        ZipMainWindow.resize(800, 600)
        ZipMainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        ZipMainWindow.setAcceptDrops(False)
        self.actionQuit = QAction(ZipMainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionOpen = QAction(ZipMainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setCheckable(False)
        self.actionOpen.setAutoRepeat(True)
        self.actionSetting = QAction(ZipMainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionExit = QAction(ZipMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setCheckable(True)
        self.actionExit.setChecked(False)
        self.actionExit.setEnabled(True)
        self.centralwidget = QWidget(ZipMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 12, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.setting_input_file = QLineEdit(self.groupBox)
        self.setting_input_file.setObjectName(u"setting_input_file")

        self.gridLayout_2.addWidget(self.setting_input_file, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.setting_button_fileopen = QPushButton(self.groupBox)
        self.setting_button_fileopen.setObjectName(u"setting_button_fileopen")

        self.gridLayout_2.addWidget(self.setting_button_fileopen, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.setting_input_thread_num = QLineEdit(self.groupBox)
        self.setting_input_thread_num.setObjectName(u"setting_input_thread_num")

        self.gridLayout_2.addWidget(self.setting_input_thread_num, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.progress_text_pregress_digital = QLabel(self.groupBox_2)
        self.progress_text_pregress_digital.setObjectName(u"progress_text_pregress_digital")

        self.gridLayout_3.addWidget(self.progress_text_pregress_digital, 1, 1, 1, 2)

        self.progress_text_speed = QLabel(self.groupBox_2)
        self.progress_text_speed.setObjectName(u"progress_text_speed")

        self.gridLayout_3.addWidget(self.progress_text_speed, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.progress_input_result = QLineEdit(self.groupBox_2)
        self.progress_input_result.setObjectName(u"progress_input_result")
        self.progress_input_result.setReadOnly(True)

        self.gridLayout_3.addWidget(self.progress_input_result, 3, 1, 1, 2)

        self.progress_pregress_bar = QProgressBar(self.groupBox_2)
        self.progress_pregress_bar.setObjectName(u"progress_pregress_bar")
        self.progress_pregress_bar.setValue(0)

        self.gridLayout_3.addWidget(self.progress_pregress_bar, 0, 1, 1, 2)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.control_button_start_pause = QPushButton(self.groupBox_3)
        self.control_button_start_pause.setObjectName(u"control_button_start_pause")

        self.gridLayout_4.addWidget(self.control_button_start_pause, 0, 0, 1, 1)

        self.control_button_stop = QPushButton(self.groupBox_3)
        self.control_button_stop.setObjectName(u"control_button_stop")

        self.gridLayout_4.addWidget(self.control_button_stop, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.groupBox_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pwd_toolBox = QToolBox(self.frame_3)
        self.pwd_toolBox.setObjectName(u"pwd_toolBox")
        self.pwd_toolBox.setMinimumSize(QSize(200, 0))
        self.pwd_toolBox.setMaximumSize(QSize(1000, 16777215))
        self.pwd_toolBox.setAutoFillBackground(False)
        self.pwd_page_1 = QWidget()
        self.pwd_page_1.setObjectName(u"pwd_page_1")
        self.pwd_page_1.setGeometry(QRect(0, 0, 348, 380))
        self.checkBox = QCheckBox(self.pwd_page_1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 0, 85, 20))
        self.label_4 = QLabel(self.pwd_page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 50, 58, 16))
        self.lineEdit = QLineEdit(self.pwd_page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(90, 50, 191, 21))
        self.lineEdit.setReadOnly(False)
        self.checkBox_2 = QCheckBox(self.pwd_page_1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(290, 50, 85, 20))
        self.label_6 = QLabel(self.pwd_page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 110, 81, 16))
        self.pwd_checkBox_1 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_1.setObjectName(u"pwd_checkBox_1")
        self.pwd_checkBox_1.setGeometry(QRect(20, 150, 51, 21))
        self.pwd_checkBox_2 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_2.setObjectName(u"pwd_checkBox_2")
        self.pwd_checkBox_2.setGeometry(QRect(90, 150, 51, 21))
        self.pwd_checkBox_3 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_3.setObjectName(u"pwd_checkBox_3")
        self.pwd_checkBox_3.setGeometry(QRect(160, 150, 51, 21))
        self.pwd_checkBox_4 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_4.setObjectName(u"pwd_checkBox_4")
        self.pwd_checkBox_4.setGeometry(QRect(230, 150, 51, 21))
        self.pwd_checkBox_5 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_5.setObjectName(u"pwd_checkBox_5")
        self.pwd_checkBox_5.setGeometry(QRect(290, 150, 51, 21))
        self.pwd_checkBox_6 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_6.setObjectName(u"pwd_checkBox_6")
        self.pwd_checkBox_6.setGeometry(QRect(20, 200, 51, 21))
        self.pwd_checkBox_7 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_7.setObjectName(u"pwd_checkBox_7")
        self.pwd_checkBox_7.setGeometry(QRect(90, 200, 51, 21))
        self.pwd_checkBox_8 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_8.setObjectName(u"pwd_checkBox_8")
        self.pwd_checkBox_8.setGeometry(QRect(160, 200, 51, 21))
        self.pwd_checkBox_9 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_9.setObjectName(u"pwd_checkBox_9")
        self.pwd_checkBox_9.setGeometry(QRect(230, 200, 51, 21))
        self.pwd_checkBox_10 = QCheckBox(self.pwd_page_1)
        self.pwd_checkBox_10.setObjectName(u"pwd_checkBox_10")
        self.pwd_checkBox_10.setGeometry(QRect(290, 200, 51, 21))
        self.pwd_toolBox.addItem(self.pwd_page_1, u"\u6570\u5b57")
        self.pwd_page_2 = QWidget()
        self.pwd_page_2.setObjectName(u"pwd_page_2")
        self.pwd_page_2.setGeometry(QRect(0, 0, 348, 380))
        self.pwd_toolBox.addItem(self.pwd_page_2, u"\u5b57\u6bcd")
        self.pwd_page_3 = QWidget()
        self.pwd_page_3.setObjectName(u"pwd_page_3")
        self.pwd_toolBox.addItem(self.pwd_page_3, u"\u5bc6\u7801\u8868")

        self.gridLayout.addWidget(self.pwd_toolBox, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.horizontalLayout)

        ZipMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ZipMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        ZipMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ZipMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        ZipMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(ZipMainWindow)

        self.pwd_toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ZipMainWindow)
    # setupUi

    def retranslateUi(self, ZipMainWindow):
        ZipMainWindow.setWindowTitle(QCoreApplication.translate("ZipMainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("ZipMainWindow", u"Quit", None))
        self.actionOpen.setText(QCoreApplication.translate("ZipMainWindow", u"Open", None))
        self.actionSetting.setText(QCoreApplication.translate("ZipMainWindow", u"Setting", None))
        self.actionExit.setText(QCoreApplication.translate("ZipMainWindow", u"Exit", None))
        self.groupBox.setTitle(QCoreApplication.translate("ZipMainWindow", u"\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("ZipMainWindow", u"\u6587\u4ef6:", None))
        self.setting_button_fileopen.setText(QCoreApplication.translate("ZipMainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("ZipMainWindow", u"\u5e76\u884c\u5ea6:", None))
        self.setting_input_thread_num.setText(QCoreApplication.translate("ZipMainWindow", u"5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ZipMainWindow", u"\u8fdb\u5ea6", None))
        self.label_3.setText(QCoreApplication.translate("ZipMainWindow", u"\u8fdb\u5ea6:", None))
        self.label_5.setText(QCoreApplication.translate("ZipMainWindow", u"\u901f\u5ea6:", None))
        self.progress_text_pregress_digital.setText(QCoreApplication.translate("ZipMainWindow", u"0/0", None))
        self.progress_text_speed.setText(QCoreApplication.translate("ZipMainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("ZipMainWindow", u"Q/S", None))
        self.label_8.setText(QCoreApplication.translate("ZipMainWindow", u"\u7ed3\u679c:", None))
        self.label_9.setText(QCoreApplication.translate("ZipMainWindow", u"\u8fdb\u5ea6\u6761:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ZipMainWindow", u"\u63a7\u5236\u5668", None))
        self.control_button_start_pause.setText(QCoreApplication.translate("ZipMainWindow", u"\u5f00\u59cb", None))
        self.control_button_stop.setText(QCoreApplication.translate("ZipMainWindow", u"\u7ed3\u675f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ZipMainWindow", u"\u65e5\u5fd7", None))
        self.checkBox.setText(QCoreApplication.translate("ZipMainWindow", u"\u542f\u7528", None))
        self.label_4.setText(QCoreApplication.translate("ZipMainWindow", u"\u9ed8\u8ba4\u6570\u5b57:", None))
        self.lineEdit.setText(QCoreApplication.translate("ZipMainWindow", u"0123456789", None))
        self.checkBox_2.setText(QCoreApplication.translate("ZipMainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.label_6.setText(QCoreApplication.translate("ZipMainWindow", u"\u5bc6\u7801\u4f4d\u6570\u5b57:", None))
        self.pwd_checkBox_1.setText(QCoreApplication.translate("ZipMainWindow", u"1", None))
        self.pwd_checkBox_2.setText(QCoreApplication.translate("ZipMainWindow", u"2", None))
        self.pwd_checkBox_3.setText(QCoreApplication.translate("ZipMainWindow", u"3", None))
        self.pwd_checkBox_4.setText(QCoreApplication.translate("ZipMainWindow", u"4", None))
        self.pwd_checkBox_5.setText(QCoreApplication.translate("ZipMainWindow", u"5", None))
        self.pwd_checkBox_6.setText(QCoreApplication.translate("ZipMainWindow", u"6", None))
        self.pwd_checkBox_7.setText(QCoreApplication.translate("ZipMainWindow", u"7", None))
        self.pwd_checkBox_8.setText(QCoreApplication.translate("ZipMainWindow", u"8", None))
        self.pwd_checkBox_9.setText(QCoreApplication.translate("ZipMainWindow", u"9", None))
        self.pwd_checkBox_10.setText(QCoreApplication.translate("ZipMainWindow", u"10", None))
        self.pwd_toolBox.setItemText(self.pwd_toolBox.indexOf(self.pwd_page_1), QCoreApplication.translate("ZipMainWindow", u"\u6570\u5b57", None))
        self.pwd_toolBox.setItemText(self.pwd_toolBox.indexOf(self.pwd_page_2), QCoreApplication.translate("ZipMainWindow", u"\u5b57\u6bcd", None))
        self.pwd_toolBox.setItemText(self.pwd_toolBox.indexOf(self.pwd_page_3), QCoreApplication.translate("ZipMainWindow", u"\u5bc6\u7801\u8868", None))
        self.menuFile.setTitle(QCoreApplication.translate("ZipMainWindow", u"File", None))
    # retranslateUi

