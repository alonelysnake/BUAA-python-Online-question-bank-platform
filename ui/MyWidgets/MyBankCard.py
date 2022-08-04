from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontMetrics, QResizeEvent
from ui.MyWidgets.BankCard import Ui_Form

from question.QuestionBank import QuestionBank


class MyBankCard(Ui_Form, QWidget):
    clickDetail = pyqtSignal(int)

    def __init__(self, parent, bank: QuestionBank, select=False):
        super(MyBankCard, self).__init__(parent)
        self.setupUi(self)
        self.bankName.setText(bank.getName())
        self.bid = bank.getBid()

        if not select:
            self.testButton.hide()

        self.detailButton.clicked.connect(self.click)
        self.testButton.clicked.connect(self.click)

    def click(self):
        self.clickDetail.emit(self.bid)
