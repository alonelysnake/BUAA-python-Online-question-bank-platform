from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from question.Question import *
from question.QuestionBank import QuestionBank

from ReviseLoadFile import Ui_MainWindow
from MyWidgets.MySelectionCard import MySelectionCard


# 上传题目时，手动修改每一道题的界面
class MyReviseLoadFile(Ui_MainWindow, QMainWindow):
    switch2mainWindow = pyqtSignal(QMainWindow)

    def __init__(self, mainWindow, bank: QuestionBank):
        super(MyReviseLoadFile, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow

        self.selectButton.clicked.connect(self.switchQuestionType)
        self.fillButton.clicked.connect(self.switchQuestionType)
        self.answerButton.clicked.connect(self.switchQuestionType)
        self.nextButton.clicked.connect(self.nextButtonOperation)
        self.addSelectionButton.clicked.connect(self.addNewSelection)

        self.bank = bank
        self.curQuestionType = CHOICE
        self.baseIndex = len(bank.getQuestions())
        self.pos = 0
        self.questionsText = []
        self.newQuestions = []

    def initAttribute(self, path):
        self.curQuestionType = CHOICE  # 0 选择 1 填空 2 解答
        self.pos = 0
        # TODO 得到题目列表(可能无法成功读取)
        self.questionsText = [1]  # 切分好的题目列表

        if not self.questionsText:
            # TODO 未找到question时
            return
        elif len(self.questionsText) == 1:
            self.nextButton.setText("完成")
        else:
            self.nextButton.setText("下一题")
        self.showQuestion()

    def nextButtonOperation(self):
        self.generateQuestion()  # 生成并存储
        self.pos += 1
        if self.pos == len(self.questionsText) - 1:
            self.nextButton.setText("完成")
            self.showQuestion()
        elif self.pos == len(self.questionsText):
            # 返回到主界面
            self.switch2mainWindow.emit(self.mainWindow)
        else:
            # TODO 展示下一道题（暂时不会用到）
            pass

    def generateQuestion(self):
        # TODO 未检查
        if self.curQuestionType == CHOICE:
            stem = self.objectQuestion.toPlainText()
            selections = []  # 选择题的选项
            answer = ""
            for selection in self.selection.children():
                if isinstance(selection, MySelectionCard):
                    selections.append(selection.textEdit.toPlainText())
                    if selection.selectButton.isChecked():
                        answer += selection.getChoice()
            analysis = self.objectExplanation.toPlainText()
            question = Question(self.baseIndex + self.pos, self.pos, stem, self.curQuestionType, answer, analysis,
                                selections)
        else:
            stem = self.subjectQuestion.toPlainText()
            answer = self.subjectAnswer.toPlainText()
            analysis = self.subjectAnswer.toPlainText()
            question = Question(self.baseIndex + self.pos, self.pos, stem, self.curQuestionType, answer, analysis, [])
        self.newQuestions.append(question)

    def switchQuestionType(self):
        if self.selectButton.isChecked():
            if self.curQuestionType != CHOICE:
                self.object2subject()
                self.curQuestionType = CHOICE
        elif self.fillButton.isChecked():
            if self.curQuestionType == CHOICE:
                self.subject2object()
            self.curQuestionType = BLANK
        else:
            if self.curQuestionType == CHOICE:
                self.subject2object()
            self.curQuestionType = ESSAY

    def object2subject(self):
        self.stackedWidget.setCurrentIndex(0)
        self.showSubjectQuestion()

    def subject2object(self):
        self.stackedWidget.setCurrentIndex(1)
        self.showObjectQuestion()

    def showQuestion(self):
        if self.curQuestionType == 0:
            self.showObjectQuestion()
        else:
            self.showSubjectQuestion()

    def showObjectQuestion(self):
        self.stackedWidget.setCurrentIndex(0)

    def showSubjectQuestion(self):
        self.stackedWidget.setCurrentIndex(1)

    def addNewSelection(self):
        newSelection = MySelectionCard(self.selectionBox)
        newSelection.setChoice(len(self.selectionBox.children()) - 1)
        self.selectionLayout.addWidget(newSelection)
