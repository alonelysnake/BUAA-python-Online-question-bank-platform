from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
import sys

from question.Question import *
from question.QuestionBank import QuestionBank
from user.User import UserUtil, CUR_USER

from ui.MainWindow import Ui_MainWindow
from ui.MyWidgets.MyQuestionCard import MyQuestionCard
from ui.MyChooseLoadFile import MyChooseLoadFile
from ui.MyChooseQuestion import MyChooseQuestion
from ui.MyRegister import MyRegister
from ui.MyLogin import MyLogin
from ui.MyAnalysis import MyAnalysis


class MyMainWindow(Ui_MainWindow, QMainWindow):
    switch2reviseFile = pyqtSignal(QMainWindow, str)  # 跳转到上传后修改的信号

    def __init__(self, mainWindow, bank: QuestionBank):
        super(MyMainWindow, self).__init__()
        self.setupUi(mainWindow)
        self.mainWindow = mainWindow
        self.questions = {}  # questions集合
        self.questionDetail.backSignal.connect(self.backFromDetail)
        self.addQuestionButton.triggered.connect(self.uploadFileEvent)
        self.selfTestButton.triggered.connect(self.selfTestEvent)
        self.registerButton.triggered.connect(self.registerEvent)
        self.loginButton.triggered.connect(self.loginEvent)
        self.logoutButton.triggered.connect(self.logoutEvent)
        self.analyseButton.triggered.connect(self.analyseEvent)
        self.questionCategoryLayout.setAlignment(Qt.AlignTop)

        self.bank = bank
        self.updateQuestions()

    # 主界面到上传界面
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

    # 主界面到自测界面
    def selfTestEvent(self):
        newWindow = QMainWindow()
        chooseWindow = MyChooseQuestion(newWindow, self, self.bank, self.questions)
        newWindow.show()

    def registerEvent(self):
        dialog = QDialog()
        registerWindow = MyRegister(dialog)
        while dialog.exec_() == 1 and not registerWindow.isRegister:
            continue

    def loginEvent(self):
        dialog = QDialog()
        loginWindow = MyLogin(dialog)
        while dialog.exec_() == 1 and not loginWindow.isLogin:
            continue

    def logoutEvent(self):
        UserUtil.logout()
        QMessageBox.information(self, "成功", "已退出登录")

    def analyseEvent(self):
        if CUR_USER.isLogin:
            newWindow = QMainWindow()
            analyseWindow = MyAnalysis(newWindow, self, self.bank)
            newWindow.show()
        else:
            QMessageBox.information(self, "错误", "请先登录")
            self.loginEvent()

    def seeDetail(self, bid, qid):
        self.menuBar.hide()
        self.stackedWidget.setCurrentIndex(1)
        question = self.questions[qid]
        self.questionDetail.show(question=question)

    def backFromDetail(self):
        self.menuBar.show()
        self.stackedWidget.setCurrentIndex(0)

    def updateQuestions(self):
        for question in self.bank.getQuestions():
            assert isinstance(question, Question)
            index = question.getIndex()
            if index not in self.questions.keys():
                self.questions[index] = question
                newQuestionCard = MyQuestionCard(self.questionCategory, index, select=False)
                self.questionCategoryLayout.addWidget(newQuestionCard)
                newQuestionCard.setText(str(question.getIndex()) + ". " + question.getStem())
                newQuestionCard.clickDetail.connect(self.seeDetail)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    bank = QuestionBank("科目一", 0)
    mainWindow = MyMainWindow(window, bank)
    # dialog.show()
    window.show()
    app.exec_()
    # print("filepath: " + chooseFile.filepath)
    # print(dialog.exec_() == QDialog.Rejected)
    sys.exit()
