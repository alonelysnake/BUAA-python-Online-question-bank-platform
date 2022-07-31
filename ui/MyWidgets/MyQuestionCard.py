from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from ui.MyWidgets.QuestionCard import Ui_Form
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo


# 题目的缩略表示
class MyQuestionCard(QWidget, Ui_Form):
    clickDetail = pyqtSignal(int)

    def __init__(self, parent, index=0, select=False):
        super(MyQuestionCard, self).__init__(parent)
        self.setupUi(self)
        self.index = index
        self.select = select  # 是否显示选择按钮
        if not select:
            self.chooseButton.hide()

        self.detialButton.clicked.connect(self.viewDetail)

    # 查看详情
    def viewDetail(self):
        self.clickDetail.emit(self.index)

    def setText(self, text):
        self.label.setText(text)

    def setChecked(self, select):
        self.chooseButton.setChecked(select)

    def isChecked(self):
        return self.chooseButton.isChecked()


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    box = MyQuestionBox(None, 0)
    box.show()
    app.exec_()
