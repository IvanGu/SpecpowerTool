# -*- coding: utf-8 -*-

"""
Module implementing pen.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Question import Ui_Dialog


class QuestionInterface(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(QuestionInterface, self).__init__(parent)
        self.setupUi(self)