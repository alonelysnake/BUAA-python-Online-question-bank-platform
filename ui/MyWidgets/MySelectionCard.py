from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from ui.MyWidgets.SelectionCard import Ui_Form


class MySelectionCard(Ui_Form, QWidget):
    def __init__(self, parent):
        super(MySelectionCard, self).__init__(parent)
        self.setupUi(self)

    def setText(self, text):
        self.textEdit.setText(text)
