from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTextEdit


# 上传题库时用的，支持拖入文件的填空框
class MyQTextEdit(QTextEdit):
    # sendmsg = pyqtSignal(object)

    def __init__(self, parent=None):
        super(MyQTextEdit, self).__init__(parent)
        self.setAcceptDrops(True)
        self.paths = set()

    def dropEvent(self, e):
        self.paths = set(self.toPlainText().split("\n"))
        newPaths = set(e.mimeData().text().replace('file:///', '').split('\n'))
        for path in newPaths:
            if (path.endswith('.pdf') or path.endswith('.png')
                or path.endswith(".jpg") or path.endswith(".jpeg")) and path not in self.paths:
                self.paths.add(path)
                self.append(path)
