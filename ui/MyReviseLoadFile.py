from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt

from ocrpart.ocrclass import Paddleocr
from question.Question import *
from question.QuestionBank import QuestionBank

from ui.ReviseLoadFile import Ui_MainWindow
from ui.MyWidgets.MySelectionCard import MySelectionCard
import os


# 上传题目时，手动修改每一道题的界面
class MyReviseLoadFile(Ui_MainWindow, QMainWindow):
    switch2mainWindow = pyqtSignal(QMainWindow)

    def __init__(self, bank: QuestionBank):
        super(MyReviseLoadFile, self).__init__()
        self.setupUi(self)
        #self.mainWindow = self

        self.selectButton.clicked.connect(self.switchQuestionType)
        self.fillButton.clicked.connect(self.switchQuestionType)
        self.answerButton.clicked.connect(self.switchQuestionType)
        self.nextButton.clicked.connect(self.nextButtonOperation)
        self.addSelectionButton.clicked.connect(self.addNewSelection)
        self.selectionLayout.setAlignment(Qt.AlignTop)

        self.bank = bank
        self.curQuestionType = CHOICE
        self.baseIndex = len(bank.getQuestions())
        self.pos = 0
        self.questionsText = []
        self.newQuestions = []

    def initAttribute(self, paths: str):
        self.curQuestionType = CHOICE
        self.pos = 0
        # 得到题目列表
        self.questionsText.clear()
        recognize = Paddleocr("", "")
        for path in set(paths.split("\n")):
            print(path)
            if os.path.exists(path):
                nms = path.split(".")
                recognize.change_img(nms[0], "", nms[1])
                for res in recognize.forward():
                    self.questionsText.append(res)
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
        print(self.pos)
        print(len(self.questionsText))
        if self.pos == len(self.questionsText) - 1:
            self.nextButton.setText("完成")
        elif self.pos == len(self.questionsText):
            # 存储并返回到主界面
            self.bank.addQuestions(self.newQuestions)
            # TODO mainwindow更新题库
            self.switch2mainWindow.emit(self)
            return
        self.showQuestion()

    # 生成question并暂存（此时未进入bank）
    def generateQuestion(self):
        stem = self.question.toPlainText()
        analysis = self.explanation.toPlainText()
        if self.curQuestionType == CHOICE:
            selections = []  # 选择题的选项
            answer = ""
            for selection in self.selectionBox.children():
                if isinstance(selection, MySelectionCard):
                    selections.append(selection.textEdit.toPlainText())
                    if selection.selectButton.isChecked():
                        answer += selection.getChoice()
            question = Question(self.baseIndex + self.pos, self.bank.getBid(), stem,
                                self.curQuestionType, answer, analysis, selections)
        else:
            answer = self.subjectAnswer.toPlainText()
            question = Question(self.baseIndex + self.pos, self.bank.getBid(),
                                stem, self.curQuestionType, answer, analysis, [])
        self.newQuestions.append(question)

    def switchQuestionType(self):
        if self.selectButton.isChecked():
            if self.curQuestionType != CHOICE:
                self.subject2object()
                self.curQuestionType = CHOICE
        elif self.fillButton.isChecked():
            if self.curQuestionType == CHOICE:
                self.object2subject()
            self.curQuestionType = BLANK
        else:
            if self.curQuestionType == CHOICE:
                self.object2subject()
            self.curQuestionType = ESSAY

    def object2subject(self):
        self.stackedWidget.setCurrentIndex(0)
        self.showSubjectQuestion()

    def subject2object(self):
        self.stackedWidget.setCurrentIndex(1)
        self.showObjectQuestion()

    def showQuestion(self):
        self.question.setText(self.questionsText[self.pos])
        self.subjectAnswer.setText("")
        self.explanation.setText("")
        for child in self.selectionBox.children():
            if isinstance(child, MySelectionCard):
                self.selectionLayout.removeWidget(child)
        if self.curQuestionType == CHOICE:
            self.showObjectQuestion()
        else:
            self.showSubjectQuestion()

    def showObjectQuestion(self):
        self.stackedWidget.setCurrentIndex(0)

    def showSubjectQuestion(self):
        self.stackedWidget.setCurrentIndex(1)

    def addNewSelection(self):
        newSelection = MySelectionCard(self.selectionBox)
        newSelection.setChoice(len(self.selectionBox.children()) - 2)
        self.selectionLayout.addWidget(newSelection)

    def closeEvent(self, event):
        print("gg")
        self.hide()
        self.switch2mainWindow.emit(self)