# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResetTime.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(248, 144)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 60, 131, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 21))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 110, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reset Os Time Info"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Please Set SUT Os Date and Time !</span></p></body></html>"))

