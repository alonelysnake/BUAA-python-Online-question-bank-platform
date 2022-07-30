import sys

from ui import WindowController,ChooseQuestion,MyChooseQuestion
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    window = MyChooseQuestion.MyChooseQuestion(mainWindow)
    #window.setupUi(mainWindow)
    mainWindow.show()
    #controller= WindowController.WindowController()
    sys.exit(app.exec_())