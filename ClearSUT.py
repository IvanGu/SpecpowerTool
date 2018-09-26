# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClearSUT.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 142)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 411, 61))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 100, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clear SUT Program"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CCS Will Shutdown All SUT Current Test Program Item</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Such As:Io Meter Test,FPGA Stress Test,Java Jvm,PTU Program</span></p></body></html>"))

