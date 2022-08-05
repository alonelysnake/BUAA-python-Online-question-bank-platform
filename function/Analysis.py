# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 16:30
# @Author  : Kazeya
# @File    : Analysis.py
# @Description :

from user.User import CUR_USER
from user.User import UserUtil
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

matplotlib.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
matplotlib.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

matplotlib.use("Qt5Agg")  # 声明使用QT5


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = None

    def plot_2d(self, logs):
        self.axes = self.fig.add_subplot(111)
        times = np.arange(1, len(logs) + 1)
        acc = []
        for log in logs:
            num = log[4].split(',')
            acc.append((log[2] - len(num)) / log[2])
        avg = sum(acc) / len(acc)
        self.axes.plot(times, acc, "go-")
        self.axes.set_xlabel('练习次数')
        self.axes.set_ylabel('正确率')
        self.axes.set_xticks(np.arange(1, len(logs) + 1))
        self.axes.axhline(y=avg, color="gray", ls='--')
        self.axes.legend(labels=('正确率', '平均正确率'))


# 运行模块
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui.WyyAnalysis import Ui_matplot_demo
from user.User import CUR_USER

class myWindow(QWidget, Ui_matplot_demo):
    def __init__(self, parent, logs=CUR_USER.getLogs(1)):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0, 0)
        self.logs = CUR_USER.getLogs(1)
        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=10, height=10, dpi=100)
        # self.F.plot_cos()

        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        # 在容器中添加一个groupbox对象，在groupbox对象中创建布局
        self.groupBox = QGroupBox(self.plt3d_module)
        self.groupBox.setMinimumSize(QSize(1100, 610))
        self.groupBox.setTitle("历史成绩分析")
        self.toolbar = None
        self.glo_plt_figure = QGridLayout(self.groupBox)
        self.open_pic()

    def open_pic(self):
        self.F = MyFigure(width=10, height=3, dpi=100)
        # self.F.plot_3d()
        self.F.plot_2d(self.logs)
        self.toolbar = NavigationToolbar(self.F, self)
        self.glo_plt_figure.addWidget(self.toolbar, 2, 0)
        self.glo_plt_figure.addWidget(self.F, 0, 0)
        self.show()
        self.glo_plt_figure.addWidget(self.F, 0, 0)

    def close_pic(self):
        self.glo_plt_figure.removeWidget(self.F)
        self.show()


def main():
    app = QApplication(sys.argv)
    UserUtil.login('123', '123')
    win = myWindow(CUR_USER.getLogs(1))
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
