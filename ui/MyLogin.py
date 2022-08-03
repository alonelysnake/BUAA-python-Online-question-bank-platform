from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

from ui.Login import Ui_Dialog
from ui.MyRegister import MyRegister

from user.User import UserUtil


class MyLogin(QDialog, Ui_Dialog):
    def __init__(self, dialog):
        super().__init__()
        self.setupUi(dialog)
        self.registerButton.clicked.connect(self.register)

        dialog.setWindowFlags(Qt.WindowCloseButtonHint)

    def accept(self):
        password = self.password.toPlainText()
        user = self.user.toPlainText()
        # TODO 不存在用户或密码不对的判断条件
        if user:
            msg = QMessageBox(QMessageBox.Retry, "错误", "已存在相同用户")
            msg.exec_()
        else:
            UserUtil.register(user, password)
            return super().accept()
        self.user.setPlainText("")
        self.password.setPlainText("")
        return None

    def register(self):
        dialog = QDialog()
        registerWindow = MyRegister(dialog)
        print("a")
        self.hide()
        print("b")
        execRes = dialog.exec_()
        while execRes != QDialog.Accepted and execRes != QDialog.Rejected:
            execRes = dialog.exec_()
        # 注册完成或取消了注册
        if execRes == QDialog.Accepted:
            # 在注册成功时已经自动完成登录，直接返回即可
            super(MyLogin, self).accept()