# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\coding\python\homework\Online-question-bank-platform\ui\ReviseLoadFile.ui'
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.question = QtWidgets.QTextEdit(self.centralwidget)
        self.question.setObjectName("question")
        self.gridLayout.addWidget(self.question, 1, 0, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page0.sizePolicy().hasHeightForWidth())
        self.page0.setSizePolicy(sizePolicy)
        self.page0.setObjectName("page0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addSelectionButton = QtWidgets.QPushButton(self.page0)
        self.addSelectionButton.setObjectName("addSelectionButton")
        self.gridLayout_2.addWidget(self.addSelectionButton, 7, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.page0)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.selectionBox = QtWidgets.QWidget()
        self.selectionBox.setGeometry(QtCore.QRect(0, 0, 272, 137))
        self.selectionBox.setObjectName("selectionBox")
        self.selectionLayout = QtWidgets.QVBoxLayout(self.selectionBox)
        self.selectionLayout.setObjectName("selectionLayout")
        self.scrollArea.setWidget(self.selectionBox)
        self.gridLayout_2.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.objectlabel_2 = QtWidgets.QLabel(self.page0)
        self.objectlabel_2.setObjectName("objectlabel_2")
        self.gridLayout_2.addWidget(self.objectlabel_2, 5, 0, 1, 1)
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.page1.setObjectName("page1")
        self.subjectLayout = QtWidgets.QVBoxLayout(self.page1)
        self.subjectLayout.setObjectName("subjectLayout")
        self.subjectlabel_1 = QtWidgets.QLabel(self.page1)
        self.subjectlabel_1.setObjectName("subjectlabel_1")
        self.subjectLayout.addWidget(self.subjectlabel_1)
        self.subjectAnswer = QtWidgets.QTextEdit(self.page1)
        self.subjectAnswer.setObjectName("subjectAnswer")
        self.subjectLayout.addWidget(self.subjectAnswer)
        self.stackedWidget.addWidget(self.page1)
        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 2, 1)
        self.explanation = QtWidgets.QTextEdit(self.centralwidget)
        self.explanation.setObjectName("explanation")
        self.gridLayout.addWidget(self.explanation, 3, 1, 1, 1)
        self.objectlabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.objectlabel_3.setObjectName("objectlabel_3")
        self.gridLayout.addWidget(self.objectlabel_3, 2, 1, 1, 1)
        self.objectlabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.objectlabel_1.setObjectName("objectlabel_1")
        self.gridLayout.addWidget(self.objectlabel_1, 0, 0, 1, 1)
        self.selectButton = QtWidgets.QRadioButton(self.centralwidget)
        self.selectButton.setChecked(True)
        self.selectButton.setObjectName("selectButton")
        self.gridLayout.addWidget(self.selectButton, 6, 2, 1, 1)
        self.fillButton = QtWidgets.QRadioButton(self.centralwidget)
        self.fillButton.setObjectName("fillButton")
        self.gridLayout.addWidget(self.fillButton, 7, 2, 1, 1)
        self.answerButton = QtWidgets.QRadioButton(self.centralwidget)
        self.answerButton.setCheckable(True)
        self.answerButton.setObjectName("answerButton")
        self.gridLayout.addWidget(self.answerButton, 8, 2, 1, 1)
        self.nextButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.nextButton, 9, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addSelectionButton.setText(_translate("MainWindow", "添加新选项"))
        self.objectlabel_2.setText(_translate("MainWindow", "选项与答案"))
        self.subjectlabel_1.setText(_translate("MainWindow", "答案"))
        self.objectlabel_3.setText(_translate("MainWindow", "答案解析"))
        self.objectlabel_1.setText(_translate("MainWindow", "问题描述"))
        self.selectButton.setText(_translate("MainWindow", "选择题"))
        self.fillButton.setText(_translate("MainWindow", "填空题"))
        self.answerButton.setText(_translate("MainWindow", "解答题"))
        self.nextButton.setText(_translate("MainWindow", "下一题"))
