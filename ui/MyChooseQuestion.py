import random

from ChooseQuestion import Ui_MainWindow
from MyWidgets.MyQuestionCard import MyQuestionCard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from question.Question import *


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
class MyChooseQuestion(QMainWindow, Ui_MainWindow):
    def __init__(self, window, parent, questions: list):
        super(MyChooseQuestion, self).__init__(parent=parent)
        self.setupUi(window)
        self.mainWindow = window
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.questions = questions
        self.tests = []
        self.curIndex = 0

        index = 0
        for question in self.questions:
            # TODO index修正
            newQuestionCard = MyQuestionCard(self.questionCategory, index, True)
            newQuestionCard.setText("问题一")
            newQuestionCard.clickDetail.connect(self.seeDetail)
            self.questionCategoryLayout.addWidget(newQuestionCard)
            index += 1

        self.manualButton.clicked.connect(self.manualGenerate)
        self.randomButton.clicked.connect(self.randomGenerate)
        self.lastButton.clicked.connect(self.jumpLastQuestion)
        self.nextButton.clicked.connect(self.jumpNextQuestion)

    def randomGenerate(self):
        num = int(min(len(self.questions) / 5, 100))
        self.tests = random.sample(self.questions, num)
        self.showTest()

    def manualGenerate(self):
        self.tests.clear()
        for card in self.questionCategory.children():
            if isinstance(card, MyQuestionCard) and card.isChecked():
                self.tests.append(self.questions[card.index])
        self.showTest()

    # 显示自测界面
    def showTest(self):
        # TODO
        for i in range(len(self.tests)):
            button = MyPushButton(i)
            button.clicked.connect(self.jumpQuestion)
            self.questionButtonsLayout.addWidget(button)
        self.curIndex = 0
        self.stackedWidget.setCurrentIndex(2)
        self.jumpQuestion(0)

    # 选题界面查看详情
    def seeDetail(self, index):
        self.stackedWidget.setCurrentIndex(1)
        print("gg")
        question = Question("问题", Type.CHOICE, "答案", "分析")
        self.questionDetail.show(question=question)

    # 从查看详情返回选题界面
    def backFromDetail(self):
        self.stackedWidget.setCurrentIndex(0)

    # 自测时跳转到第index道题
    def jumpQuestion(self, index: int):
        # TODO 先存储当前界面的题
        # 根据index的值做一些非常规判断
        if index == len(self.tests):
            self.submit()
            return
        if index == 0:
            self.lastButton.setEnabled(False)
        else:
            self.lastButton.setEnabled(True)
        if index == len(self.tests) - 1:
            self.nextButton.setText("交卷")
        else:
            self.nextButton.setText("下一题")
        question = self.tests[index]
        assert isinstance(question, Question)
        self.stem.setText(question.getStem())
        if question.getType() == Type.CHOICE:
            # TODO 显示选项
            pass
        else:
            self.answerText.setText("")
            self.testQuestionType.setCurrentIndex(0)

    def jumpLastQuestion(self):
        self.jumpQuestion(self.curIndex - 1)

    def jumpNextQuestion(self):
        self.jumpQuestion(self.curIndex + 1)

    def submit(self):
        # 跳转道反馈界面
        pass
