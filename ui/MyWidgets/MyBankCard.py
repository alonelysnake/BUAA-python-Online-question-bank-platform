from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontMetrics, QResizeEvent
from ui.MyWidgets.BankCard import Ui_Form

from question.QuestionBank import QuestionBank

class MyAnalysisCard(Ui_Form, QWidget):
    def __init__(self, parent, bank:QuestionBank):
        super(MyAnalysisCard, self).__init__(parent)
        self.setupUi(self)
        self.bankName.setText()

