from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from question.Question import *
from question.QuestionBank import QuestionBank

from ui.ReviseLoadFile import Ui_MainWindow
from ui.MyWidgets.MySelectionCard import MySelectionCard
import ocrpart.ocrclass
#from ocrpart.ocrclass import Paddleocr
import os


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

    def initAttribute(self, paths: str):
        self.curQuestionType = CHOICE  # 0 选择 1 填空 2 解答
        self.pos = 0
        # 得到题目列表
        self.questionsText.clear()
        recognize = Paddleocr()
        for path in paths.split("\n"):
            if os.path.exists(path):
                recognize.img_path = path
                recognize.type = path.split(".")[1]
                self.questionsText.append(recognize.get_result())
            else:
                # TODO 路径非法时操作
                pass

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
        elif self.pos == len(self.questionsText):
            # 存储并返回到主界面
            self.bank.addQuestions(self.newQuestions)
            self.switch2mainWindow.emit(self.mainWindow)
            return
        self.showQuestion()

    # 生成question并暂存（此时未进入bank）
    def generateQuestion(self):
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
        self.objectQuestion.setText(self.questionsText[self.pos])
        self.stackedWidget.setCurrentIndex(0)

    def showSubjectQuestion(self):
        self.subjectQuestion.setText(self.questionsText[self.pos])
        self.stackedWidget.setCurrentIndex(1)

    def addNewSelection(self):
        newSelection = MySelectionCard(self.selectionBox)
        newSelection.setChoice(len(self.selectionBox.children()) - 1)
        self.selectionLayout.addWidget(newSelection)
