# -*- coding: utf-8 -*-
# @Time    : 2022/7/30 18:53
# @Author  : Kazeya
# @File    : DatabaseUtil.py
# @Description :

import pymysql

class DB():
    def __init__(self):
        if not hasattr(DB,"_first_init"):
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='837826068', charset='utf8')
            self.cursor = self.conn.cursor()
            DB._first_init = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(DB, "_instance"):
            DB._instance = object.__new__(cls)
        return DB._instance

    def selectDatabase(self,name):
        self.cursor.execute('use ' + name + 's')

    def option(self,op,baseName,id):
        if op == "select":
            op += " *"
        op += " from "
        self.cursor.execute(op + baseName + " where id=" + "'" + str(id) + "'")

    def createBank(self,name,type):
        self.cursor.execute('use base_name')
        self.cursor.execute("insert into " + type + "_name(name) values('" + name + "')")
        self.conn.commit()
        self.cursor.execute('use ' + type + 's')
        sql = """
        (
            id int not null primary key auto_increment,
            bid int not null,
            stem text(21845) not null,
            type int not null,
            answer text(21845) not null,
            analysis text(21845) not null,
            optionA text(1024) null,
            optionB text(1024) null,
            optionC text(1024) null,
            optionD text(1024) null,
            optionE text(1024) null
        )default charset=utf8;
        """
        self.cursor.execute('create table ' + name + sql)
        self.conn.commit()
