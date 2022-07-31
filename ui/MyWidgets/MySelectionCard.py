from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from ui.MyWidgets.SelectionCard import Ui_Form


class MySelectionCard(Ui_Form, QWidget):
    def __init__(self, parent):
        super(MySelectionCard, self).__init__(parent)
        self.setupUi(self)

    # 设置选项的ABCD
    def setChoice(self, index):
        self.selectButton.setText(chr(ord('A') + index) + ". ")

    # 得到ABCD
    def getChoice(self):
        return self.selectButton.text().split(".")[0]

    def setText(self, text):
        self.textEdit.setText(text)
