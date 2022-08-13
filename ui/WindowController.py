import sys

from PyQt5.QtWidgets import *

from ui.MyMainWindow import MyMainWindow
from ui.MyReviseLoadFile import MyReviseLoadFile
from question.QuestionBank import QuestionBank


class WindowController:
    def __init__(self, bank: QuestionBank):
        #window = QMainWindow()
        self.mainWindow = MyMainWindow(bank)
        self.mainWindow.switch2reviseFile.connect(self.showReviseFile)
        #window.show()
        self.mainWindow.show()

        #window = QMainWindow()
        self.reviseFileWindow = MyReviseLoadFile(bank)
        self.reviseFileWindow.switch2mainWindow.connect(self.showMainWindow)

    # 显示上传后修改的界面
    def showReviseFile(self, window, path):
        window.hide()
        self.reviseFileWindow.initAttribute(path)
        self.reviseFileWindow.show()
        print("load revise load file success")

    def showMainWindow(self, window):
        window.hide()
        self.mainWindow.updateQuestions()
        self.mainWindow.show()
        print("come back to mainwindow success")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    bank = QuestionBank("科目一", 0)
    controller = WindowController(bank)
    app.exec_()
