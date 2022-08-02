# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:25
# @Author  : Kazeya
# @File    : ExamGeneration.py
# @Description : 自动或手动生成题单

# 选择题库->题单名字—>自动或手动->题量

from DatabaseUtil import DB

class ExamGeneration:

    @classmethod
    def generate(cls, bankId: int, listName: str, amount: int, index:list, model="auto"):
        db = DB()
        db.cursor.execute('use base_name')
        db.cursor.execute("select * from bank_name where id='" + str(bankId) + "'")
        bankName = db.cursor.fetchone()[1]
        db.createBank(listName,1)
        if model == "auto":
            # print("insert into " + listName + " select * from banks." + bankName + " where id>=((select max(id) from banks." + bankName + " )-(select min(id) from banks." + bankName + "))* RAND() + (SELECT MIN(Id) FROM banks." + bankName + ") limit " + str(amount))
            db.cursor.execute(
                "insert into " + listName + " select * from banks." + bankName + \
                " where id>=((select max(id) from banks." + bankName + " )-(select min(id) from banks." + bankName + \
                "))* RAND() + (SELECT MIN(Id) FROM banks." + bankName + ") limit " + str(amount))
            db.conn.commit()
        else:
            for i in index:
                db.cursor.execute(
                    "insert into " + listName + " select * from banks." + bankName + \
                    " where id=" + "'" + str(i) + "'")
            db.conn.commit()

if __name__ == '__main__':
    # ExamGeneration.generate(8,'科目一试卷1',20,[])
    db = DB()
    listName = '科目一试卷1'
    bankName = '科目一'
    amount = 20
    db.cursor.execute("use lists")
    index = [10,17,19,21,22,25,26,30]
    for i in index:
        db.cursor.execute(
            "insert into " + listName + " select * from banks." + bankName + \
            " where id=" + "'" + str(i) + "'")
    db.conn.commit()