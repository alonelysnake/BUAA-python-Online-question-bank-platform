import random

from ui.ChooseQuestion import Ui_MainWindow
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt

from question.Question import *
from question.QuestionBank import QuestionBank


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
    def __init__(self, window, parent, bank: QuestionBank, questions: dict):
        super(MyChooseQuestion, self).__init__(parent=parent)
        self.setupUi(window)
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.questionCategoryLayout.setAlignment(Qt.AlignTop)
        self.selectionsLayout.setAlignment(Qt.AlignTop)

        self.mainWindow = window
        self.bank = bank
        self.questions = questions
        self.tests = []
        self.curIndex = 0

        self.answers = []
        for index in self.questions.keys():
            newQuestionCard = MyQuestionCard(self.questionCategory, index, True)
            newQuestionCard.setText(str(index))
            newQuestionCard.clickDetail.connect(self.seeDetail)
            self.questionCategoryLayout.addWidget(newQuestionCard)
        self.manualButton.clicked.connect(self.manualGenerate)
        self.randomButton.clicked.connect(self.randomGenerate)
        self.lastButton.clicked.connect(self.jumpLastQuestion)
        self.nextButton.clicked.connect(self.jumpNextQuestion)

    def randomGenerate(self):
        num = int(min(len(self.questions) / 5, 100))
        self.tests = random.sample(list(self.questions.values()), num)
        self.answers.clear()
        for i in range(num):
            self.answers.append("")
        self.showTest()

    def manualGenerate(self):
        self.tests.clear()
        self.answers.clear()
        for card in self.questionCategory.children():
            if isinstance(card, MyQuestionCard) and card.isChecked():
                self.tests.append(self.questions[card.index])
                self.answers.append("")
        self.showTest()

    # 显示自测界面
    def showTest(self):
        for i in range(len(self.tests)):
            button = MyPushButton(i)
            button.jump2Question.connect(self.jumpQuestion)
            self.questionButtonsLayout.addWidget(button)
        self.curIndex = 0
        self.stackedWidget.setCurrentIndex(2)
        self.jumpQuestion(0)

    # 选题界面查看详情
    def seeDetail(self, index):
        self.stackedWidget.setCurrentIndex(1)
        question = self.bank.getQuestion(index)
        self.questionDetail.show(question=question)

    # 从查看详情返回选题界面
    def backFromDetail(self):
        self.stackedWidget.setCurrentIndex(0)

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
        children = self.questionButtons.children()[1:]
        for i in range(len(self.tests)):
            if self.answers[i] != self.tests[i].getAnswer():
                children[i].setStyleSheet("color:red")
            else:
                children[i].setStyleSheet("color:green")
