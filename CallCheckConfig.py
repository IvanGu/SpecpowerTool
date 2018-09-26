# -*- coding: utf-8 -*-

"""
Module implementing pen.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from CheckConfig import Ui_Dialog


class CheckConfigInterface(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(CheckConfigInterface, self).__init__(parent)
        self.setupUi(self)