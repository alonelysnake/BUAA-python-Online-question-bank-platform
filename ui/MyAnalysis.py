from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import datetime

# from function.ScoreAnalysis import ApplicationWindow

from question.QuestionBank import QuestionBank
from question.Question import Question
from user.User import CUR_USER

from function.Analysis import myWindow

from ui.Analysis import Ui_MainWindow
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from ui.MyWidgets.MyBankCard import MyBankCard
from ui.MyWidgets.MyHistoryCard import MyHistoryCard


class MyAnalysis(Ui_MainWindow, QMainWindow):
    def __init__(self, window, parent, bank: QuestionBank):
        super(MyAnalysis, self).__init__(parent=parent)
        self.setupUi(window)

        self.analysisCardsLayout.setAlignment(Qt.AlignTop)
        self.wrongQuestionsLayout.setAlignment(Qt.AlignTop)
        self.graph.logs = CUR_USER.getLogs(bank.getBid())
        print(bank.getBid())
        print(CUR_USER.getLogs(bank.getBid()))

        self.bank = bank

        self.analysisButton.clicked.connect(self.analysisButtonEvent)
        self.wrongButton.clicked.connect(self.wrongButtonEvent)

        self.loadHistory()
        self.loadWrongQuestionCards()

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
        # TODO 创建一个新的子窗口，展示分析结果
        # analysisWindow = ApplicationWindow(CUR_USER.getLogs(bid))
        # analysisWindow.show()
        pass

    # 查看错题的详细内容
    def seeWrongDetail(self, bid, qid):
        self.stackedWidget.setCurrentIndex(3)
        self.questionInfo.show(self.bank.getQuestion(qid))

    # 题单
    def loadHistory(self):
        for log in CUR_USER.getLogs(self.bank.getBid()):
            historyCard = MyHistoryCard(self.analysisCards)
            historyCard.setName(log[3])
            assert isinstance(log[5], datetime.datetime)
            historyCard.setTime(str(log[5]).split('.')[0])
        # for bank in QuestionBank.getLists():
        #     assert isinstance(bank, QuestionBank)
        #     analysisCard = MyBankCard(self.analysisCards, bank)
        #     analysisCard.clickDetail.connect(self.seeAnalysis)
        #     self.analysisCardsLayout.addWidget(analysisCard)

    def loadWrongQuestionCards(self):
        for question in CUR_USER.getMistakes(self.bank.getBid()):
            assert isinstance(question, Question)
            newQuestionCard = MyQuestionCard(self.wrongQuestions, question)
            newQuestionCard.setText(str(question.getIndex()) + ". " + question.getStem())
            newQuestionCard.clickDetail.connect(self.seeWrongDetail)
            self.wrongQuestionsLayout.addWidget(newQuestionCard)
