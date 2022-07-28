import sys

from ui import WindowController
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # window = MyReviseLoadFile.MyReviseLoadFile(mainWindow)
    # mainWindow.show()
    controller= WindowController.WindowController()
    sys.exit(app.exec_())