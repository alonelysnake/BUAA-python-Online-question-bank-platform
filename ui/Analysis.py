# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\coding\python\homework\Online-question-bank-platform\ui\Analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.analysisButton = QtWidgets.QPushButton(self.centralwidget)
        self.analysisButton.setObjectName("analysisButton")
        self.gridLayout.addWidget(self.analysisButton, 0, 0, 1, 1)
        self.wrongButton = QtWidgets.QPushButton(self.centralwidget)
        self.wrongButton.setObjectName("wrongButton")
        self.gridLayout.addWidget(self.wrongButton, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.analysisCards = QtWidgets.QWidget()
        self.analysisCards.setGeometry(QtCore.QRect(0, 0, 754, 242))
        self.analysisCards.setObjectName("analysisCards")
        self.analysisCardsLayout = QtWidgets.QVBoxLayout(self.analysisCards)
        self.analysisCardsLayout.setObjectName("analysisCardsLayout")
        self.scrollArea.setWidget(self.analysisCards)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        print("aa")
        self.graph = myWindow(self.page0)
        print("bb")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setObjectName("graph")
        self.gridLayout_2.addWidget(self.graph, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.wrongQuestions = QtWidgets.QWidget()
        self.wrongQuestions.setGeometry(QtCore.QRect(0, 0, 754, 494))
        self.wrongQuestions.setObjectName("wrongQuestions")
        self.wrongQuestionsLayout = QtWidgets.QVBoxLayout(self.wrongQuestions)
        self.wrongQuestionsLayout.setObjectName("wrongQuestionsLayout")
        self.scrollArea_2.setWidget(self.wrongQuestions)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.questionInfo = myWindow(self.page3)
        self.questionInfo.setObjectName("questionInfo")
        self.gridLayout_5.addWidget(self.questionInfo, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page3)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.analysisButton.setText(_translate("MainWindow", "成绩分析"))
        self.wrongButton.setText(_translate("MainWindow", "错题统计"))
from function.Analysis import myWindow
