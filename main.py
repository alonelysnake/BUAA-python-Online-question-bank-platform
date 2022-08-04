import sys

from PyQt5.QtWidgets import QApplication
from question.QuestionBank import QuestionBank
from DatabaseUtil import DB
from ui.WindowController import WindowController


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # window = MyReviseLoadFile.MyReviseLoadFile(mainWindow)
    # mainWindow.show()
    # controller= WindowController.WindowController()
    # sys.exit(app.exec_())
    db = DB()
    db.initial()
    db.createBank('科目一',0,0)
    bank = QuestionBank("科目一", 0)
    #db.createBank('科目一试卷1',1,bank.getBid())
    app = QApplication(sys.argv)
    controller = WindowController(bank)
    app.exec_()