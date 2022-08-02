# -*- coding: utf-8 -*-
# @Time    : 2022/8/2 15:54
# @Author  : Kazeya
# @File    : ScoreAnalysis.py
# @Description : 成绩分析工具类

from __future__ import unicode_literals
from user.User import CUR_USER
from user.User import UserUtil
import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self,logs):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(6, 5)))
        layout.addWidget(NavigationToolbar(static_canvas, self))
        layout.addWidget(static_canvas)

        #dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        #layout.addWidget(dynamic_canvas)
        #layout.addWidget(NavigationToolbar(dynamic_canvas, self))

        self._static_ax = static_canvas.figure.subplots()
        times = np.arange(1,len(logs)+1)
        acc = []
        for log in logs:
            num = log[4].split(',')
            acc.append((log[2]-len(num))/log[2])
        avg = sum(acc) / len(acc)
        self._static_ax.plot(times, acc, "go-")
        self._static_ax.set_xlabel('练习次数')
        self._static_ax.set_ylabel('正确率')
        self._static_ax.set_xticks(np.arange(1,len(logs)+1))
        self._static_ax.axhline(y=avg, color="gray",ls='--')
        self._static_ax.legend(labels=('正确率', '平均正确率'))

        #self._dynamic_ax = dynamic_canvas.figure.subplots()
        #t = np.linspace(0, 10, 101)
        # Set up a Line2D.
        #self._line, = self._dynamic_ax.plot(t, np.sin(t + time.time()))
        #self._timer = dynamic_canvas.new_timer(50)
        #self._timer.add_callback(self._update_canvas)
        #self._timer.start()

    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)
    UserUtil.login('Kazeya','123456')
    app = ApplicationWindow(CUR_USER.getLogs(1))
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()