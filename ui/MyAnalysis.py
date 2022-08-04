from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from question.QuestionBank import QuestionBank
from question.Question import Question
from user.User import CUR_USER

from ui.Analysis import Ui_MainWindow
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo
from ui.MyWidgets.MyQuestionCard import MyQuestionCard


class MyAnalysis(Ui_MainWindow, QMainWindow):
    def __init__(self, window: QMainWindow, parent, bank: QuestionBank):
        super(MyAnalysis, self).__init__(parent=parent)
        self.setupUi(QMainWindow)
        self.banksLayout.setAlignment(Qt.AlignTop)
        self.wrongQuestionsLayout.setAlignment(Qt.AlignTop)

        self.banks = {bank.getBid(): bank}

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
    def seeAnalysis(self, bid):
        self.stackedWidget.setCurrentIndex(2)
        # TODO 实际分析结果显示
        pass

    # 查看错题的详细内容
    def seeWrongDetail(self, bid, qid):
        self.stackedWidget.setCurrentIndex(3)
        self.questionInfo.show(self.banks[bid].getQuestion(qid))

    def loadBankCards(self):
        pass

    def loadWrongQuestionCards(self):
        for question in CUR_USER.getMistakes():
            assert isinstance(question, Question)
            newQuestionCard = MyQuestionCard(self.wrongQuestions, question.getIndex(),
                                             question.getBid(), question.getStem())
            self.wrongQuestionsLayout.addWidget(newQuestionCard)
        pass
