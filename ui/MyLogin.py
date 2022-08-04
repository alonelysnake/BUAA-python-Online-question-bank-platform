from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QEvent
import sys

from ui.Login import Ui_Dialog
from ui.MyRegister import MyRegister

from user.User import UserUtil


class MyLogin(QDialog, Ui_Dialog):
    def __init__(self, dialog):
        super().__init__()
        self.setupUi(dialog)
        self.registerButton.clicked.connect(self.register)
        self.buttonBox.accepted.connect(self.accept)
        self.isLogin = False

        dialog.setWindowFlags(Qt.WindowCloseButtonHint)

    def accept(self):
        password = self.password.toPlainText()
        user = self.user.toPlainText()
        # TODO 不存在用户或密码不对的判断条件
        if not UserUtil.login(user, password):
            QMessageBox.information(self, "错误", "用户名或密码错误")
        else:
            self.isLogin = True
            QMessageBox.information(self, "成功", "登录成功！")
        self.user.setPlainText("")
        self.password.setPlainText("")
        return super(MyLogin, self).accept()

    def register(self):
        dialog = QDialog()
        registerWindow = MyRegister(dialog)
        self.hide()
        execRes = dialog.exec_()
        while execRes == 1 and not registerWindow.isRegister:
            execRes = dialog.exec_()
        print(dialog.size())
