from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

from .ReviseLoadFile import Ui_MainWindow


class MyReviseLoadFile(Ui_MainWindow, QMainWindow):
    switch2mainWindow = pyqtSignal(QMainWindow)

    def __init__(self, mainWindow):
        super(MyReviseLoadFile, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow

        self.selectButton.clicked.connect(self.switchQuestionType)
        self.fillButton.clicked.connect(self.switchQuestionType)
        self.answerButton.clicked.connect(self.switchQuestionType)
        self.nextButton.clicked.connect(self.nextButtonOperation)

        self.initAttribute("")

    def initAttribute(self, path):
        self.questionType = 0  # 0 选择 1 填空 2 解答
        self.pos = 0
        # TODO 得到题目列表(可能无法成功读取)
        self.questionList = [1]  # 切分好的题目列表

        if not self.questionList:
            # TODO 未找到question时
            pass
        elif len(self.questionList) == 1:
            self.nextButton.setText("完成")
        else:
            self.nextButton.setText("下一题")

    def nextButtonOperation(self):
        self.pos += 1
        if self.pos == len(self.questionList) - 1:
            self.nextButton.setText("完成")
        elif self.pos == len(self.questionList):
            # TODO 读取完成，保存到文件
            pass
            # TODO 返回到主界面
            self.switch2mainWindow.emit(self.mainWindow)
            pass
        else:
            # TODO 展示下一道题
            pass

    def switchQuestionType(self):
        if self.selectButton.isChecked():
            if self.questionType != 0:
                self.object2subject()
                self.questionType = 0
        elif self.fillButton.isChecked():
            if self.questionType == 0:
                self.subject2object()
            self.questionType = 1
        else:
            if self.questionType == 0:
                self.subject2object()
            self.questionType = 2

    def object2subject(self):
        self.stackedWidget.setCurrentIndex(0)
        # TODO 更新题面的表示

    def subject2object(self):
        self.stackedWidget.setCurrentIndex(1)
        # TODO 更新题面的表示

    def showNextQuestion(self):
        # TODO 读取下一道题
        pass
        if self.questionType == 0:
            self.showObjectQuestion()
        else:
            self.showSubjectQuestion()

    def showObjectQuestion(self):
        pass

    def showSubjectQuestion(self):
        pass
