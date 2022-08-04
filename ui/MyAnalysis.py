from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from question.QuestionBank import QuestionBank
from question.Question import Question

from ui.Analysis import Ui_MainWindow
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo


class MyAnalysis(Ui_MainWindow, QMainWindow):
    def __init__(self, window: QMainWindow, parent, bank: QuestionBank):
        super(MyAnalysis, self).__init__(parent=parent)
        self.setupUi(QMainWindow)

        self.banks = {bank.getBid(): bank}

        self.bid = 0  # 查看详细分析页面时的题库id
        self.qid = 0  # 查看错题详细内容时错题的id

        self.analysisButton.clicked.connect(self.analysisButtonEvent)
        self.wrongButton.clicked.connect(self.wrongButton)

        self.analysisButtonEvent()

    def analysisButtonEvent(self):
        self.stackedWidget.setCurrentIndex(0)
        self.analysisButton.setDisabled(True)
        self.wrongButton.setDisabled(False)

    def wrongButtonEvent(self):
        self.stackedWidget.setCurrentIndex(1)
        self.wrongButton.setDisabled(True)
        self.analysisButton.setDisabled(False)

    # 查看详细的分析结果图
    def seeAnalysis(self):
        self.stackedWidget.setCurrentIndex(2)
        # TODO 实际分析结果显示
        pass

    # 查看错题的详细内容
    def seeWrongDetail(self):
        self.stackedWidget.setCurrentIndex(3)
        self.questionInfo.show(self.banks[self.bid].getQuestion(self.qid))
