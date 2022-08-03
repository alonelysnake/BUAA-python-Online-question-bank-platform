from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from ui.Register import Ui_Dialog

from user.User import UserUtil


class MyRegister(Ui_Dialog, QDialog):
    def __init__(self, dialog):
        super().__init__()
        self.setupUi(dialog)
        self.buttonBox.accepted.connect(self.accept)
        print("aaaa")
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)

    def accept(self):
        password = self.password.toPlainText()
        check = self.checkAgain.toPlainText()
        user = self.user.toPlainText()
        # TODO 已存在用户的判断条件
        if user:
            msg = QMessageBox(QMessageBox.Retry, "错误", "已存在相同用户")
            msg.exec_()
        # 两次密码不一致
        elif password != check:
            msg = QMessageBox(QMessageBox.Retry, '错误', "两次密码不一致")
            msg.exec_()
        else:
            UserUtil.register(user, password)
            #TODO 注册的话会自动登录刚注册的用户
            return super().accept()
        self.user.setPlainText("")
        self.password.setPlainText("")
        self.checkAgain.setPlainText("")
