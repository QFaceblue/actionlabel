# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/actionlabel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(902, 511)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source_line = QtWidgets.QLineEdit(Form)
        self.source_line.setObjectName("source_line")
        self.horizontalLayout.addWidget(self.source_line)
        self.source_btn = QtWidgets.QPushButton(Form)
        self.source_btn.setObjectName("source_btn")
        self.horizontalLayout.addWidget(self.source_btn)
        self.dest_line = QtWidgets.QLineEdit(Form)
        self.dest_line.setObjectName("dest_line")
        self.horizontalLayout.addWidget(self.dest_line)
        self.dest_btn = QtWidgets.QPushButton(Form)
        self.dest_btn.setObjectName("dest_btn")
        self.horizontalLayout.addWidget(self.dest_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 163, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.last_btn = QtWidgets.QPushButton(Form)
        self.last_btn.setObjectName("last_btn")
        self.horizontalLayout_2.addWidget(self.last_btn)
        self.img_label = QtWidgets.QLabel(Form)
        self.img_label.setObjectName("img_label")
        self.horizontalLayout_2.addWidget(self.img_label)
        self.next_btn = QtWidgets.QPushButton(Form)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_2.addWidget(self.next_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 163, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_5.addWidget(self.start_btn)
        self.progress_label = QtWidgets.QLabel(Form)
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayout_5.addWidget(self.progress_label)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_0 = QtWidgets.QPushButton(Form)
        self.label_0.setObjectName("label_0")
        self.horizontalLayout_3.addWidget(self.label_0)
        self.label_1 = QtWidgets.QPushButton(Form)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_3.addWidget(self.label_1)
        self.label_2 = QtWidgets.QPushButton(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QPushButton(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QPushButton(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QPushButton(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QPushButton(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_7 = QtWidgets.QPushButton(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QPushButton(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.delete_btn = QtWidgets.QPushButton(Form)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_4.addWidget(self.delete_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "??????????????????"))
        self.source_btn.setText(_translate("Form", "??????????????????"))
        self.dest_btn.setText(_translate("Form", "?????????????????????"))
        self.last_btn.setText(_translate("Form", "????????????"))
        self.img_label.setText(_translate("Form", "??????"))
        self.next_btn.setText(_translate("Form", "????????????"))
        self.start_btn.setText(_translate("Form", "???????????????"))
        self.progress_label.setText(_translate("Form", "??????"))
        self.label_0.setText(_translate("Form", "??????"))
        self.label_1.setText(_translate("Form", "??????"))
        self.label_2.setText(_translate("Form", "??????"))
        self.label_3.setText(_translate("Form", "??????"))
        self.label_4.setText(_translate("Form", "????????????"))
        self.label_5.setText(_translate("Form", "?????????"))
        self.label_6.setText(_translate("Form", "???????????????"))
        self.label_7.setText(_translate("Form", "????????????"))
        self.label_8.setText(_translate("Form", "?????????"))
        self.delete_btn.setText(_translate("Form", "??????"))
