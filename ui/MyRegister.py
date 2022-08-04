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
        self.isRegister = False
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)

    def accept(self):
        password = self.password.toPlainText()
        check = self.checkAgain.toPlainText()
        user = self.user.toPlainText()
        if password == "" or user == "":
            QMessageBox.information(self, "错误", "用户名或密码不能为空")
        elif password != check:
            QMessageBox.information(self, "错误", "两次密码不一致")
        elif not UserUtil.register(user, password):
            QMessageBox.information(self, "错误", "已存在相同用户")
        else:
            self.isRegister = True
            QMessageBox.information(self, "成功", "注册成功！")
        self.user.setPlainText("")
        self.password.setPlainText("")
        self.checkAgain.setPlainText("")
        return super().accept()
