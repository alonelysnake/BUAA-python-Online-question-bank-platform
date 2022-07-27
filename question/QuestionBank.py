import pandas as pd
from Question import Question
import os
from Question import Type

class QuestionBank:
    def __init__(self, name):
        self._name = name
        self._list = []

    def addQuestion(self, question):
        self._list.append(question.toList())

    def addQuestions(self, questions):
        for question in questions:
            self.addQuestion(question)

    def deleteQuestion(self, question):
        # todo
        self._list.remove(question)

    def deleteQuestions(self, questions):
        for question in questions:
            self.deleteQuestion(question)

    def getQuestion(self, stem):
        # todo 查询方法
        return self._list

    def getQuestions(self):
        return self._list

    def readFromFile(self, filePath):
        qdata = pd.read_csv(filePath,encoding='gbk')
        for data in qdata.values:
            self.addQuestion(Question(data[0],data[1],data[2],data[3]))

    def readFromeFile(self):
        qdata = pd.read_csv('../data/' + self._name + '.csv', encoding='gbk')
        for data in qdata.values:
            self.addQuestion(Question(data[0],data[1],data[2],data[3]))

    def createBank(self):
        open('../data/' + self._name + '.csv','w',encoding='gbk')

    def saveBank(self):
        df = pd.DataFrame(data=self._list,columns=['stem','type','answer','analysis'])
        df.to_csv('../data/' + self._name + '.csv',index=False)

if __name__ == '__main__':
    bank = QuestionBank("科目四")
    bank.createBank()
    bank.addQuestion(Question('a',Type.BLANK,'a','a'))
    bank.saveBank()
    print(bank.getQuestions())