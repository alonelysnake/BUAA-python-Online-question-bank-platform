from ui.MyWidgets.QuestionInfo import Ui_Form
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from question.Question import *


class MyQuestionInfo(Ui_Form, QWidget):
    backSignal = pyqtSignal()

    def __init__(self, parent):
        super(MyQuestionInfo, self).__init__(parent)
        self.setupUi(self)
        self.seeAnswerFlag.clicked.connect(self.showAnswer)
        self.backButton.clicked.connect(self.back)

    def show(self, question: Question = None):
        if question:
            # 主客观题的差异化设置
            if question.getType() == Type.CHOICE:
                self.setObjectQuestion(question)
            else:
                self.setSubjectQuestion(question)
            # 相同的设置
            self.seeAnswerFlag.setChecked(False)
            self.answerText.setText("这里是答案")
            self.answerText.hide()
        super(Ui_Form, self).show()

    def setObjectQuestion(self, question: Question):
        self.stackedWidget.setCurrentIndex(1)
        # 设置选项
        newSelection = QCheckBox()
        self.objectQuestion.setText(question.getStem())
        self.objectQuestion.setText("这里是问题题干\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\ngg\n\n\ngg\n\ng")
        # TODO 根据question设置
        newSelection.setText("选项的内容")
        newSelection.setCheckable(True)
        newSelection.setChecked(False)
        self.selectionBoxLayout.addWidget(newSelection)
        print("choice")

    def setSubjectQuestion(self, question: Question):
        self.stackedWidget.setCurrentIndex(0)
        self.subjectQuestion.setText(question.getStem())
        self.subjectQuestion.setText("这里是问题题干")

    def showAnswer(self):
        if self.seeAnswerFlag.isChecked():
            self.answerText.show()
        else:
            self.answerText.hide()

    def back(self):
        self.backSignal.emit()
