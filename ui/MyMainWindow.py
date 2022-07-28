from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSignal
import sys

from .MainWindow import Ui_MainWindow
from .MyChooseLoadFile import MyChooseLoadFile


class MyMainWindow(Ui_MainWindow, QMainWindow):
    switch2reviseFile = pyqtSignal(QMainWindow, str)  # 跳转到上传后修改的信号

    def __init__(self, mainWindow):
        super(MyMainWindow, self).__init__()
        self.setupUi(mainWindow)
        self.addQuestionButton.triggered.connect(self.uploadFileEvent)
        self.mainWindow = mainWindow

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
