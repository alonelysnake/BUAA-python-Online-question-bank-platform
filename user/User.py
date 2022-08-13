# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 16:53
# @Author  : Kazeya
# @File    : User.py
# @Description :用户类
import datetime
import time

from DatabaseUtil import DB
from question.Question import Question
from question.QuestionBank import QuestionBank

db = DB()


class User:
    def __init__(self):
        self.name = None
        self.id = None

    def setInfo(self, id, name):
        self.name = name
        self.id = id

    def addLike(self, bid: int, qid: int):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        db.cursor.execute(
            "insert into " + str(self.id) + "_likes(bid,qid) values('" + str(bid) + "','" + str(qid) + "')")
        db.conn.commit()

    def isLike(self,bid:int,qid:int) -> bool:
        if not self.isLogin:
            return False
        db.selectDatabase('data')
        # print('select * from ' + str(self.id) + "_likes where bid='" + str(bid) + "' and qid='" + str(qid) + "'")
        db.cursor.execute('select * from ' + str(self.id) + "_likes where bid='" + str(bid) + "' and qid='" + str(qid) + "'")
        logs = db.cursor.fetchall()
        return len(logs) != 0

    def isWrong(self,bid:int,qid:int) -> bool:
        if not self.isLogin:
            return False
        db.selectDatabase('data')
        db.cursor.execute(
            'select * from ' + str(self.id) + "_mistakes where bid='" + str(bid) + "' and qid='" + str(qid) + "'")
        logs = db.cursor.fetchall()
        return len(logs) != 0

    def delLike(self, bid: int, qid: int):
        if not self.isLogin:
            return
        db.selectDatabase('data')
        db.cursor.execute(
            "delete from " + str(self.id) + "_likes where bid='" + str(bid) + "' and qid='" + str(qid) + "'")
        db.conn.commit()

    # isWrong:0->正确，1->错误
    def addExercise(self, question:Question, isWrong: int):
        if not self.isLogin:
            return
        bid = question.getBid()
        qid = question.getId()
        db.selectDatabase('data')
        table = str(self.id) + "_mistakes(bid,qid,wrong_times,exc_times)"
        values = " values('" + str(bid) + "','" + str(qid) + "','" + str(isWrong) + "','1')"
        condition = " on duplicate key update wrong_times=wrong_times+" + str(isWrong) + ", exc_times=exc_times+1"
        db.cursor.execute("insert into " + table + values + condition)
        db.conn.commit()

    # mistakes: "index1,index2,index3,...", date:"yyyy-mm-dd hh:mm:ss"
    def addListExercise(self,questionBank:QuestionBank, mistakes:list, date: str):
        if not self.isLogin:
            return
        mistakes = ','.join(mistakes)
        print(mistakes)
        lid = questionBank.getBid()
        listName = questionBank.getName()
        bid = questionBank.getFid()
        db.selectDatabase('list')
        db.cursor.execute("select count(*) from " + listName)
        qsum = db.cursor.fetchone()[0]
        db.selectDatabase('data')
        values = "('" + str(bid) + "','" + str(lid) + "','" + str(
            qsum) + "','" + listName + "','" + mistakes + "','" + date + "')"
        db.cursor.execute("insert into " + str(self.id) + "_logs(bid,lid,qsum, name,mistakes,date) values" + values)
        db.conn.commit()

    def getMistakes(self, bid=-1):
        if not self.isLogin:
            return
        table = str(self.id) + "_mistakes"
        questions = []
        db.selectDatabase('data')
        if bid == -1:
            db.cursor.execute("select * from " + table)
            mistakes = db.cursor.fetchall()
        else:
            db.cursor.execute("select qid from " + table + " where wrong_times>'0'")
            mistakes = db.cursor.fetchall()
        db.cursor.execute("use base_name")
        db.cursor.execute("select name from bank_name where id='" + str(bid) + "'")
        bankName = db.cursor.fetchone()[0]
        db.selectDatabase('bank')
        qid = "('" + str(mistakes[0][0]) + "'"
        for m in mistakes[1:]:
            qid += ",'" + str(m[0]) + "'"
        qid += ")"
        # print(qid)
        db.cursor.execute("select * from " + bankName + " where id in " + qid)
        logs = db.cursor.fetchall()
        for log in logs:
            # print(log[0])
            options = [log[-5],log[-4],log[-3],log[-2],log[-1]]
            questions.append(Question(log[0],log[1],log[2],log[3],log[4],log[5],options))
        return questions

    def getLogs(self, bid=-1):
        if not self.isLogin:
            return
        table = str(self.id) + "_logs"
        if bid == -1:
            db.selectDatabase('data')
            db.cursor.execute("select * from " + table)
            logs = db.cursor.fetchall()
        else:
            logs = db.fetchAll('data', table, 'bid', str(bid),'*')
        return logs

    @property
    def isLogin(self) -> bool:
        if self.id:
            return True
        else:
            print("用户未登录")
            return False


CUR_USER = User()


class UserUtil:
    @classmethod
    def login(cls, name: str, pwd: str) -> bool:
        user = db.fetchOne('data', 'users', 'name', name)
        if user is None or user[2] != pwd:
            print("用户名或密码错误")
            return False
        CUR_USER.setInfo(user[0], user[1])
        return True

    @classmethod
    def logout(cls):
        CUR_USER.setInfo(None, None)

    @classmethod
    def register(cls, name, pwd) -> bool:
        user = db.fetchOne('data', 'users', 'name', name)
        if user is not None:
            print("用户名已存在")
            return False
        db.cursor.execute("insert into users(name,pwd) values('" + name + "','" + pwd + "')")
        db.conn.commit()
        user = db.fetchOne('data', 'users', 'name', name)
        sql = str(user[0]) + """_likes(
            bid int not null,
            qid int not null,
            unique(bid,qid)
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        sql = str(user[0]) + """_mistakes(
            bid int not null,
            qid int not null,
            wrong_times int not null,
            exc_times int not null,
            unique(bid,qid)
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        sql = str(user[0]) + """_logs(
            bid int not null,
            lid int not null,
            qsum int not null,
            name text(128) not null,
            mistakes text(512),
            date datetime
        )default charset=utf8;
        """
        db.cursor.execute("create table " + sql)
        db.conn.commit()
        return True


if __name__ == '__main__':
    CUR_USER.addLike(1, 1)
    UserUtil.login('123', '123')
    bank = QuestionBank('科目一试卷1',1)
    CUR_USER.addListExercise(bank,['1','2','3'],'2022-12-05 11:12:13')
    print(CUR_USER.isLike(1,3))
