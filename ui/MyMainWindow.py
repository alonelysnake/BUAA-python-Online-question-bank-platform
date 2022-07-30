from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal
import sys

from question.Question import *

from MainWindow import Ui_MainWindow
from MyWidgets.MyQuestionCard import MyQuestionCard
from MyChooseLoadFile import MyChooseLoadFile
from MyChooseQuestion import MyChooseQuestion


class MyMainWindow(Ui_MainWindow, QMainWindow):
    switch2reviseFile = pyqtSignal(QMainWindow, str)  # 跳转到上传后修改的信号

    def __init__(self, mainWindow):
        super(MyMainWindow, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.stackedWidget.setCurrentIndex(0)
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.addQuestionButton.triggered.connect(self.uploadFileEvent)
        self.selfTestButton.triggered.connect(self.selfTestEvent)

        # TODO 从题库中读取所有题目并简略显示
        question = Question("问题", Type.CHOICE, "答案", "分析")
        newQuestionCard = MyQuestionCard(self.questionCategory, 0, False)
        newQuestionCard.setText("问题一")
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
        # TODO 跳转到自测界面
        newWindow = QMainWindow()
        chooseWindow = MyChooseQuestion(newWindow, self)
        self.menu.hide()
        newWindow.show()
        print("gg")
        pass

    def seeDetail(self, index):
        self.stackedWidget.setCurrentIndex(1)
        question = Question("问题", Type.CHOICE, "答案", "分析")
        self.questionDetail.show(question=question)

    def backFromDetail(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    mainWindow = MyMainWindow(window)
    # dialog.show()
    window.show()
    app.exec_()
    # print("filepath: " + chooseFile.filepath)
    # print(dialog.exec_() == QDialog.Rejected)
    sys.exit()
