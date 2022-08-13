from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from ui.ChooseLoadFile import Ui_chooseLoadFile


# 选择要上传题库的文件界面
class MyChooseLoadFile(QDialog, Ui_chooseLoadFile):
    def __init__(self, chooseLoadFile):
        super().__init__()
        self.setupUi(chooseLoadFile)
        self.buttonBox.accepted.connect(self.accept)
        self.filepath = ""
        self.choose.clicked.connect(self.file)

        chooseLoadFile.setWindowFlags(Qt.WindowCloseButtonHint)

    def file(self):
        newPaths = QFileDialog.getOpenFileNames(self, "open file dialog", "C:\\users\\administrator\\Desktop",
                                                "支持格式 (*.jpg *.jpeg *.png *.pdf)")
        for path in newPaths[0]:
            self.textEdit.append(path)

    # 成功返回时要记录文件路径
    def accept(self):
        self.filepath = self.textEdit.toPlainText()
        print("read filepath success")
        return super().accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QDialog()
    chooseFile = MyChooseLoadFile(dialog)
    # dialog.show()
    print(dialog.exec_() == QDialog.Accepted)
    print("filepath: " + chooseFile.filepath)
    # print(dialog.exec_() == QDialog.Rejected)
    sys.exit()
