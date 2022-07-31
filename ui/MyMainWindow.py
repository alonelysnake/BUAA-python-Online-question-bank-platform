from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal
import sys

from question.Question import *
from question.QuestionBank import QuestionBank

from MainWindow import Ui_MainWindow
from MyWidgets.MyQuestionCard import MyQuestionCard
from MyChooseLoadFile import MyChooseLoadFile
from MyChooseQuestion import MyChooseQuestion


class MyMainWindow(Ui_MainWindow, QMainWindow):
    switch2reviseFile = pyqtSignal(QMainWindow, str)  # 跳转到上传后修改的信号

    def __init__(self, mainWindow, bank: QuestionBank):
        super(MyMainWindow, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.questions = []  # questions集合
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.addQuestionButton.triggered.connect(self.uploadFileEvent)
        self.selfTestButton.triggered.connect(self.selfTestEvent)

        self.bank = bank
        self.questions = self.bank.getQuestions()
        for question in self.questions:
            assert isinstance(question, Question)
            index = question.getIndex()
            newQuestionCard = MyQuestionCard(self.questionCategory, index, False)
            newQuestionCard.setText(question.getIndex())
            newQuestionCard.clickDetail.connect(self.seeDetail)
            self.questionCategoryLayout.addWidget(newQuestionCard)

    def uploadFileEvent(self):
        dialog = QDialog()
        uploadWindow = MyChooseLoadFile(dialog)
        if dialog.exec_() == QDialog.Accepted:
            # TODO 识别文件并跳转到修改界面
            self.switch2reviseFile.emit(self.mainWindow, uploadWindow.filepath)
            pass
        else:
            # 取消读取，正常返回
            pass

    def selfTestEvent(self):
        newWindow = QMainWindow()
        chooseWindow = MyChooseQuestion(newWindow, self, self.bank)
        newWindow.show()

    def seeDetail(self, index):
        self.menuBar.hide()
        self.stackedWidget.setCurrentIndex(1)
        question = self.questions[index]
        self.questionDetail.show(question=question)

    def backFromDetail(self):
        self.menuBar.show()
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    bank = QuestionBank("科目一", 0)
    mainWindow = MyMainWindow(window, bank)
    # dialog.show()
    window.show()
    app.exec_()
    # print("filepath: " + chooseFile.filepath)
    # print(dialog.exec_() == QDialog.Rejected)
    sys.exit()
