from PyQt5.QtWidgets import *

from ui.MyWidgets.HistoryCard import Ui_Form


class MyHistoryCard(Ui_Form, QWidget):
    def __init__(self, parent):
        super(MyHistoryCard, self).__init__(parent=parent)

    def setName(self, name):
        self.name.setText(name)

    def setTime(self, time):
        self.time.setText(time)
