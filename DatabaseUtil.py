# -*- coding: utf-8 -*-
# @Time    : 2022/7/30 18:53
# @Author  : Kazeya
# @File    : DatabaseUtil.py
# @Description :

import pymysql

class DB():
    LOC = ['bank', 'list']

    def __init__(self):
        if not hasattr(DB,"_first_init"):
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset='utf8')
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

    def createBank(self,name:str,type:int):
        self.cursor.execute('use base_name')
        self.cursor.execute("insert into " + self.LOC[type] + "_name(name) values('" + name + "')")
        self.conn.commit()
        self.cursor.execute('use ' + self.LOC[type] + 's')
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

    def initial(self):
        if not self.hasBase('base_name'):
            self.createBase("base_name",["bank_name","list_name"])
        if not self.hasBase('banks'):
            self.createBase("banks", [])
        if not self.hasBase('lists'):
            self.createBase("lists", [])

    def hasBase(self,baseName) -> bool:
        self.cursor.execute("show databases like '" + baseName + "'")
        base = self.cursor.fetchall()
        if len(base) == 0:
            return False
        else:
            return True

    def createBase(self,name,tables):
        self.cursor.execute('create database ' + name)
        self.conn.commit()
        self.cursor.execute('use ' + name)
        sql = """
        (
            id int not null primary key auto_increment,
            name text(1024) not null
        )default charset=utf8;
        """
        for table in tables:
            self.cursor.execute('create table ' + table + sql)
        self.conn.commit()