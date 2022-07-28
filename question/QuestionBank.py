# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:21
# @Author  : Kazeya
# @File    : QuestionBank.py
# @Description : 题库、题单类

import pandas as pd
from question.Question import Question
from question.Question import Type

class QuestionBank:
    loc = ['bank', 'list']

    # type 0->题库，1->题单
    def __init__(self, name, type):
        # todo 检查重名
        self._type = type
        self._name = name
        self._list = []
        self.readFromFile()

    def addQuestion(self, question:list):
        self._list.append(question)

    def addQuestions(self, questions):
        for question in questions:
            self.addQuestion(question)

    def deleteQuestion(self, index):
        self._list.remove(index)

    def deleteQuestions(self, indexs):
        for index in indexs:
            self.deleteQuestion(index)

    def getQuestion(self, index):
        return Question(self._list[index][0],self._list[index][1],self._list[index][2],self._list[index][3])

    def getQuestions(self):
        return self._list

    def readFromFileWithPath(self, filePath):
        qdata = pd.read_csv(filePath,encoding='utf-8')
        for data in qdata.values:
            self.addQuestion(data)

    def readFromFile(self):
        try:
            qdata = pd.read_csv(self.getPath(), encoding='utf-8')
        except:
            self.createBank()
            return
        for data in qdata.values:
            self.addQuestion(data)

    def createBank(self):
        open(self.getPath(),'w',encoding='utf-8')

    def saveBank(self):
        df = pd.DataFrame(data=self._list,columns=['stem','type','answer','analysis'])
        df.to_csv(self.getPath(),index=False)

    def sort(self):
        self._list.sort(key=lambda x:x[1])

    def getPath(self):
        return '../data/' + self.loc[self._type] + '/' + self._name + '.csv'

if __name__ == '__main__':
    bank = QuestionBank("科目一", 0)
    for i in range(150):
        bank.addQuestion([chr(i + ord('a')),i%3 + 1,'b','b'])
    bank.saveBank()
    print(bank.getQuestions())