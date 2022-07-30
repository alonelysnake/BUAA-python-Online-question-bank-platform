# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:21
# @Author  : Kazeya
# @File    : QuestionBank.py
# @Description : 题库、题单类

import pymysql
from DatabaseUtil import DB
import pandas as pd

from question.Question import Question

class QuestionBank:
    LOC = ['bank', 'list']

    # type 0->题库，1->题单
    def __init__(self, name, type):
        self._type = type
        self._name = name
        db = DB()
        db.cursor.execute('use base_name')
        db.cursor.execute("select * from " + self.LOC[self._type] + "_name where name=" + "'" + name + "'")
        self._id = db.cursor.fetchone()[0]

    def addQuestion(self, question:Question):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        sql = '(bid,stem,type,answer,analysis)'
        db.cursor.execute("insert into " + self._name + sql + 'values(' + question.toString() + ')')
        db.conn.commit()
        db.cursor.execute("select * from " + self._name + " where id=(select max(id) from " + self._name + ")")
        id = db.cursor.fetchone()[0]
        op = ord('A')
        for option in question.getOptions():
            db.cursor.execute("update " + self._name + " set option" + chr(op) + "='" + option + "' " + "where id=" + str(id))
            db.conn.commit()
            op += 1

    def addQuestions(self, questions):
        for question in questions:
            self.addQuestion(question)

    def deleteQuestion(self, id):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.option("delete",self._name,id)
        db.conn.commit()

    def deleteQuestions(self, ids):
        for id in ids:
            self.deleteQuestion(id)

    def getQuestion(self, id):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.option("select",self._name,id)
        question = db.cursor.fetchone()
        options = [question[-5],question[-4],question[-3],question[-2],question[-1]]
        return Question(question[0],question[1],question[2],question[3],question[4],question[5],options)

    def getQuestions(self):
        db = DB()
        db.selectDatabase(self.LOC[self._type])
        db.cursor.execute("select * from " + self._name)
        questions = db.cursor.fetchall()
        return questions

'''
    def readFromFileWithPath(self, filePath):
        qdata = pd.read_csv(filePath,encoding='utf-8')
        for data in qdata.values:
            self.addQuestion(data)

    def createBank(self):
        open(self.getPath(),'w',encoding='utf-8')

    def saveBank(self):
        qList = sorted(self._list.values(),key=lambda x:x[2])
        df = pd.DataFrame(data=qList,columns=['id','stem','type','answer','analysis','options'])
        df.to_csv(self.getPath(),index=False)

    def getPath(self):
        return './data/' + self.LOC[self._type] + '/' + self._name + '.csv'
'''

if __name__ == '__main__':
    db = DB()
    #db.createBank("科目一","bank")
    bank = QuestionBank("科目一", 0)
    # for i in range(150):
    #     bank.addQuestion(Question(1,0,chr(i+ord('a')),i%3+1,'bad','cc',['a','b','c']))
    print(bank.getQuestions())