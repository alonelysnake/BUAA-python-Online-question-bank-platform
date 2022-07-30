from ChooseQuestion import Ui_MainWindow
from PyQt5.QtWidgets import *


# 自测前生成题单界面
class MyChooseQuestion(QMainWindow, Ui_MainWindow):
    def __init__(self, window, parent):
        super(MyChooseQuestion, self).__init__(parent=parent)
        self.setupUi(window)
        self.mainWindow = window
