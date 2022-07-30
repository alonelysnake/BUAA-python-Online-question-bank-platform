import sys

from PyQt5.QtWidgets import *

from MyMainWindow import MyMainWindow
from MyReviseLoadFile import MyReviseLoadFile


class WindowController:
    def __init__(self):
        window = QMainWindow()
        self.mainWindow = MyMainWindow(window)
        self.mainWindow.switch2reviseFile.connect(self.showReviseFile)
        window.show()

        window = QMainWindow()
        self.reviseFileWindow = MyReviseLoadFile(window)
        self.reviseFileWindow.switch2mainWindow.connect(self.showMainWindow)

    # 显示上传后修改的界面
    def showReviseFile(self, window, path):
        window.hide()
        self.reviseFileWindow.initAttribute(path)
        self.reviseFileWindow.mainWindow.show()
        print("load revise load file success")

    def showMainWindow(self, window):
        window.hide()
        self.mainWindow.mainWindow.show()
        print("come back to mainwindow success")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = WindowController()
    app.exec_()
