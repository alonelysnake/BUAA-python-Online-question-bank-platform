import random

from ui.ChooseQuestion import Ui_MainWindow
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from ui.MyWidgets.MyBankCard import MyBankCard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt

from question.Question import *
from question.QuestionBank import QuestionBank
from user.User import CUR_USER
from function.ExamGeneration import ExamGeneration

import datetime


class MyPushButton(QPushButton):
    jump2Question = pyqtSignal(int)

    def __init__(self, index: int):
        super(MyPushButton, self).__init__()
        self.index = index
        self.setText("第" + str(index + 1) + "题")
        self.clicked.connect(self.jump)

    def jump(self):
        self.jump2Question.emit(self.index)


# 自测前生成题单界面
class MyChooseQuestion(Ui_MainWindow, QMainWindow):
    def __init__(self, window, parent, bank: QuestionBank):
        super(MyChooseQuestion, self).__init__(parent=parent)
        self.setupUi(window)
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.addBankButton.clicked.connect(self.jumpBankGenerate)
        self.backButton.clicked.connect(self.back2BankChoose)
        self.questionCategoryLayout.setAlignment(Qt.AlignTop)
        self.selectionsLayout.setAlignment(Qt.AlignTop)
        self.answerLabel.hide()
        self.groundTruth.hide()

        self.mainWindow = window
        self.banks = {}
        self.updateBanks()
        self.bank = bank
        self.testBank = None
        self.tests = []
        self.curIndex = 0
        self.answers = []

        self.manualButton.clicked.connect(self.manualGenerate)
        self.randomButton.clicked.connect(self.randomGenerate)
        self.lastButton.clicked.connect(self.jumpLastQuestion)
        self.nextButton.clicked.connect(self.jumpNextQuestion)
        self.chooseLikeButton.clicked.connect(self.chooseFilter)
        self.chooseWrongButton.clicked.connect(self.chooseFilter)

    def randomGenerate(self):
        # TODO 题单名
        num = int(min(len(self.bank.getQuestions()) / 5 + 1, 100))
        ExamGeneration.generate(self.bank.getBid(), self.newBankName.toPlainText(), num, [], "auto")
        self.updateBanks()
        self.back2BankChoose()

    def manualGenerate(self):
        indexList = []
        for card in self.questionCategory.children():
            if isinstance(card, MyQuestionCard) and card.isChecked():
                indexList.append(card.getIndex())
        ExamGeneration.generate(self.bank.getBid(), self.newBankName.toPlainText(), len(indexList), indexList, "manual")
        self.updateBanks()
        self.back2BankChoose()

    # 显示自测界面
    def showTest(self, bid: int):
        self.testBank = self.banks[bid]
        self.tests = self.banks[bid].getQuestions()
        for i in range(len(self.tests)):
            button = MyPushButton(i)
            button.jump2Question.connect(self.jumpQuestion)
            self.questionButtonsLayout.addWidget(button)
            self.answers.append("")
        self.curIndex = 0
        self.stackedWidget.setCurrentIndex(2)
        self.jumpQuestion(0)

    # 选题界面查看详情
    def seeDetail(self, bid, qid):
        self.stackedWidget.setCurrentIndex(1)
        question = self.bank.getQuestion(qid)
        self.questionDetail.show(question=question)

    # 从查看详情返回questionCategory界面
    def backFromDetail(self):
        self.stackedWidget.setCurrentIndex(0)

    # 跳转到生成题单界面
    def jumpBankGenerate(self):
        self.stackedWidget.setCurrentIndex(0)
        self.loadQuestionCategory(self.bank, True)
        self.randomButton.show()
        self.manualButton.show()
        self.newBankName.setPlainText("")
        self.newBankName.show()
        self.label.show()

    # 回到题单选择界面
    def back2BankChoose(self):
        self.stackedWidget.setCurrentIndex(3)

    # 自测时跳转到第index道题
    def jumpQuestion(self, index: int):
        # 先存储当前界面的题
        self.storeAnswer()
        # 根据index的值做一些非常规判断
        if index == len(self.tests):
            self.submit()
            return
        self.lastButton.setEnabled(index != 0)  # 不为第一个题时才可以点击
        if index == len(self.tests) - 1:
            self.nextButton.setText("交卷")
        else:
            self.nextButton.setText("下一题")
        # 显示跳转到的题
        self.curIndex = index
        question = self.tests[index]
        assert isinstance(question, Question)
        self.stem.setText(question.getStem())
        self.groundTruth.setText(question.getAnswer() + "\n" + question.getAnalysis())
        if question.getType() == CHOICE:
            # 先清空
            for selection in self.selections.children():
                if isinstance(selection, QCheckBox):
                    self.selectionsLayout.removeWidget(selection)
            selectChar = ord("A")
            for selection in question.getOptions():
                if not selection:
                    continue
                newSelection = QCheckBox()
                newSelection.setText(chr(selectChar) + ". " + selection)
                newSelection.setChecked(self.answers[index].count(chr(selectChar)) != 0)  # 加载原来的答案
                self.selectionsLayout.addWidget(newSelection)
                selectChar += 1
            self.testQuestionType.setCurrentIndex(1)
        else:
            self.answerText.setText(self.answers[index])  # 加载原来的答案
            self.testQuestionType.setCurrentIndex(0)

    def storeAnswer(self):
        assert isinstance(self.tests[self.curIndex], Question)
        answer = ""
        if self.tests[self.curIndex].getType() == CHOICE:
            for select in self.selections.children():
                if isinstance(select, QCheckBox) and select.isChecked():
                    answer += select.text().split(".")[0]
        else:
            answer = self.answerText.toPlainText()
        self.answers[self.curIndex] = answer

    def jumpLastQuestion(self):
        self.jumpQuestion(self.curIndex - 1)

    def jumpNextQuestion(self):
        self.jumpQuestion(self.curIndex + 1)

    def submit(self):
        # 简单显示，只给出是否正确
        if self.groundTruth.isHidden():
            self.answerLabel.show()
            self.groundTruth.show()
            children = self.questionButtons.children()[1:]
            wrongs = []
            for i in range(len(self.tests)):
                if self.answers[i] != self.tests[i].getAnswer():
                    children[i].setStyleSheet("color:red")
                    wrongs.append(str(self.tests[i].getIndex()))
                    CUR_USER.addExercise(self.tests[i], 1)
                else:
                    children[i].setStyleSheet("color:green")
                    CUR_USER.addExercise(self.tests[i], 0)
            CUR_USER.addListExercise(self.testBank, wrongs, datetime.datetime.now())

    # 查看某一题单详细信息时的槽函数（和选题生成题单共用一个界面）
    def seeBankDetail(self, bid: int):
        self.stackedWidget.setCurrentIndex(0)
        self.randomButton.hide()
        self.manualButton.hide()
        self.label.hide()
        self.newBankName.hide()
        self.loadQuestionCategory(self.banks[bid], False)

    def chooseFilter(self):
        self.loadQuestionCategory(self.bank, True, self.chooseLikeButton.isChecked(),
                                  self.chooseWrongButton.isChecked())

    # 加载某一题单（或题库）的所有questionCard
    def loadQuestionCategory(self, bank: QuestionBank, select: bool, selLike: bool = False, selWrong: bool = False):
        for widget in self.questionCategory.children():
            if isinstance(widget, MyQuestionCard):
                self.questionCategoryLayout.removeWidget(widget)
        for question in bank.getQuestions():
            assert isinstance(question, Question)
            bid = question.getBid()
            qid = question.getIndex()
            if not ((selLike and not CUR_USER.isLike(bid, qid)) or (selWrong and not CUR_USER.isWrong(bid, qid))):
                newQuestionCard = MyQuestionCard(self.questionCategory, question, select=select)
                newQuestionCard.clickDetail.connect(self.seeDetail)
                self.questionCategoryLayout.addWidget(newQuestionCard)

    def updateBanks(self):
        for bank in QuestionBank.getLists():
            if not bank.getBid() in self.banks.keys():
                newBankCard = MyBankCard(self.bankCategory, bank, True)
                newBankCard.clickDetail.connect(self.seeBankDetail)
                newBankCard.clickTest.connect(self.showTest)
                self.bankCategoryLaout.addWidget(newBankCard)
                self.banks[bank.getBid()] = bank
