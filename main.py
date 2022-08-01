import sys

from PyQt5.QtWidgets import QApplication
from question.QuestionBank import QuestionBank
from question.Question import Question
from function.ExamGeneration import ExamGeneration
from DatabaseUtil import DB


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # window = MyReviseLoadFile.MyReviseLoadFile(mainWindow)
    # mainWindow.show()
    # controller= WindowController.WindowController()
    # sys.exit(app.exec_())
    db = DB()
    db.initial()
    db.createBank('科目一',0)
