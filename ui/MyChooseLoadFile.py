from PyQt5.QtWidgets import QApplication, QDialog
import sys

from .ChooseLoadFile import Ui_chooseLoadFile


class MyChooseLoadFile(QDialog, Ui_chooseLoadFile):
    def __init__(self, chooseLoadFile):
        super().__init__()
        self.setupUi(chooseLoadFile)
        self.buttonBox.accepted.connect(self.accept)
        self.filepath = ""

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
