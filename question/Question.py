# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:20
# @Author  : Kazeya
# @File    : Question.py
# @Description : 题目类

from enum import Enum


class Type(Enum):
    CHOICE = 1
    BLANK = 2
    ESSAY = 3


class Question:
    def __init__(self, stem:str, type:Type, answer:str, analysis:str):
        self._analysis = analysis
        self._type = type
        if type == Type.CHOICE:
            answer = "".join(sorted(answer))
            answer = answer.upper()
        self._answer = answer
        self._stem = stem

    def __hash__(self):
        return hash(self._stem)

    def __eq__(self, other):
        return self._stem == other._stem

    def judge(self, answer) -> bool:
        if self._type == Type.ESSAY:
            raise Exception("这是一道主观题")
        if self._type == Type.CHOICE:
            answer = "".join(sorted(answer))
            answer = answer.upper()
        return answer == self._answer

    def toList(self):
        return [self._stem,self._type,self._answer,self._analysis]

    def getAnalysis(self):
        return self._analysis

    def getAnswer(self):
        return self._answer

    def getStem(self):
        return self._stem

    def getType(self):
        return self._type

