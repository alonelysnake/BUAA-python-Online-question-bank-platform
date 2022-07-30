# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:20
# @Author  : Kazeya
# @File    : Question.py
# @Description : 题目类

CHOICE = 1
BLANK = 2
ESSAY = 3


class Question:
    # choice->1,blank->2,essay->3
    def __init__(self, id:int, bid:int, stem:str, type:int, answer:str, analysis:str, options:list):
        self._bid = bid
        self._id = id
        self._options = options
        self._analysis = analysis
        self._type = type
        if type == CHOICE:
            answer = "".join(sorted(answer))
            answer = answer.upper()
        self._answer = answer
        self._stem = stem

    def __hash__(self) -> int:
        return hash([self._bid,self._id])

    def __eq__(self, other):
        return self._id == other._id and self._bid == other._bid

    def judge(self, answer) -> bool:
        if self._type == ESSAY:
            raise Exception("这是一道主观题")
        if self._type == CHOICE:
            answer = "".join(sorted(answer))
            answer = answer.upper()
        return answer == self._answer

    def toString(self):
        return str("'" + str(self._bid) + "'" + ',' + "'" + self._stem + "'" + ',' + "'" + str(self._type) + "'" + ',' + "'" + str(self._answer) + "'" + ',' + "'" + str(self._analysis) + "'")

    def toList(self):
        return [self._id, self._bid, self._stem, self._type, self._answer, self._analysis, self._options]

    def getAnalysis(self):
        return self._analysis

    def getAnswer(self):
        return self._answer

    def getStem(self):
        return self._stem

    def getType(self):
        return self._type

    def getIndex(self):
        return self._id

    def getOptions(self):
        return self._options

    def getBid(self):
        return self._bid
