# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:21
# @Author  : Kazeya
# @File    : QuestionBank.py
# @Description : 题库、题单类

import sys
sys.path.append("..")

import pandas as pd

from question.Question import Question

class QuestionBank:
    LOC = ['bank', 'list']

    # type 0->题库，1->题单
    def __init__(self, name, type):
        # todo 检查重名
        self._type = type
        self._name = name
        self._list = {}
        self.readFromFile()

    def addQuestion(self, question:Question):
        self._list[question.getIndex()] = question.toList()

    def addQuestions(self, questions):
        for question in questions:
            self.addQuestion(question)

    def deleteQuestion(self, index):
        self._list.pop(index)

    def deleteQuestions(self, indexs):
        for index in indexs:
            self.deleteQuestion(index)

    def getQuestion(self, index):
        return Question(self._list[index][0],self._list[index][1],self._list[index][2],self._list[index][3],self._list[index][4],self._list[index][5])

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
            self.addQuestion(Question(data[0],data[1],data[2],data[3],data[4],data[5]))

    def createBank(self):
        open(self.getPath(),'w',encoding='utf-8')

    def saveBank(self):
        qList = sorted(self._list.values(),key=lambda x:x[2])
        df = pd.DataFrame(data=qList,columns=['id','stem','type','answer','analysis','options'])
        df.to_csv(self.getPath(),index=False)

    def getPath(self):
        return './data/' + self.LOC[self._type] + '/' + self._name + '.csv'

if __name__ == '__main__':
    bank = QuestionBank("科目一", 0)
    for i in range(150):
        bank.addQuestion(Question(0,chr(i+ord('a')),i%3+1,'bad','cc',['a','b','c']))
    bank.saveBank()
    print(bank.getQuestions())