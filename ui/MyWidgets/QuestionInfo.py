# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\coding\python\homework\Online-question-bank-platform\ui\MyWidgets\QuestionInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.backButton = QtWidgets.QCommandLinkButton(Form)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 776, 521))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.subjectQuestion = QtWidgets.QTextBrowser(self.page0)
        self.subjectQuestion.setObjectName("subjectQuestion")
        self.gridLayout_2.addWidget(self.subjectQuestion, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.objectQuestion = QtWidgets.QTextBrowser(self.page1)
        self.objectQuestion.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.objectQuestion.setObjectName("objectQuestion")
        self.horizontalLayout.addWidget(self.objectQuestion)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page1)
        self.scrollArea_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.selectionBox = QtWidgets.QWidget()
        self.selectionBox.setGeometry(QtCore.QRect(0, 0, 360, 198))
        self.selectionBox.setObjectName("selectionBox")
        self.selectionBoxLayout = QtWidgets.QVBoxLayout(self.selectionBox)
        self.selectionBoxLayout.setObjectName("selectionBoxLayout")
        self.scrollArea_2.setWidget(self.selectionBox)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page1)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.seeAnswerFlag = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.seeAnswerFlag.setObjectName("seeAnswerFlag")
        self.gridLayout_3.addWidget(self.seeAnswerFlag, 2, 0, 1, 1)
        self.answerText = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.answerText.setObjectName("answerText")
        self.gridLayout_3.addWidget(self.answerText, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.backButton.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "题目描述"))
        self.seeAnswerFlag.setText(_translate("Form", "查看答案"))
