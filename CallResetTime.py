# -*- coding: utf-8 -*-

"""
Module implementing pen.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from ResetTime import Ui_Dialog


class ResetOSDateTimeInterface(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(ResetOSDateTimeInterface, self).__init__(parent)
        self.setupUi(self)