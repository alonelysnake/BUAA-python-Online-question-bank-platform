from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFontMetrics, QResizeEvent
from ui.MyWidgets.QuestionCard import Ui_Form
from ui.MyWidgets.MyQuestionInfo import MyQuestionInfo

from question.Question import Question

# 题目的缩略表示
class MyQuestionCard(QWidget, Ui_Form):
    clickDetail = pyqtSignal(int, int)

    def __init__(self, parent, question:Question, select=False):
        super(MyQuestionCard, self).__init__(parent)
        self.setupUi(self)
        self.index = question.getIndex()
        self.bid = question.getBid()
        self.text = question.getStem()  # 题目文本
        self.select = select  # 是否显示选择按钮
        if not select:
            self.chooseButton.hide()
        self.detialButton.clicked.connect(self.viewDetail)

    def getIndex(self):
        return self.index

    # 查看详情
    def viewDetail(self):
        print(self.chooseButton.width())
        print(self.detialButton.width())
        print(self.label.width())
        self.clickDetail.emit(self.bid, self.index)

    def setText(self, text):
        self.text = text

    def setChecked(self, select):
        self.chooseButton.setChecked(select)

    def isChecked(self):
        return self.chooseButton.isChecked()

    def resizeEvent(self, qResizeEvent: QResizeEvent):
        super(MyQuestionCard, self).resizeEvent(qResizeEvent)
        metrics = QFontMetrics(self.label.font())
        self.label.setText(metrics.elidedText(self.text, Qt.ElideRight, qResizeEvent.size().width() - 150))


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    box = MyQuestionBox(None, 0)
    box.show()
    app.exec_()
