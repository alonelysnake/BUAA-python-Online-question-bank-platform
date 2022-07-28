from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTextEdit


class MyQTextEdit(QTextEdit):
    sendmsg = pyqtSignal(object)

    def __init__(self, parent=None):
        super(MyQTextEdit, self).__init__(parent)
        self.setAcceptDrops(True)
        self.path = ""

    def dragEnterEvent(self, e):
        self.path = e.mimeData().text().replace('file:///', '')
        if self.path.endswith('.pdf') or self.path.endswith('.png'):
            e.accept()
        else:
            self.path = ""
            e.ignore()

    def dropEvent(self, e):
        super().dropEvent(e)  # 加这一句即可
        # 只有在框内松开才会读取
        self.setText(self.path)
        # 发射信号
        self.sendmsg.emit(self.path)
