# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 17:25
# @Author  : Kazeya
# @File    : ExamGeneration.py
# @Description : 自动或手动生成题单

# 选择题库->题单名字—>自动或手动->题量

from question.QuestionBank import QuestionBank
import random

class ExamGeneration:

    @classmethod
    def generate(cls,bankName: str, listName: str, amount: int, index, model="auto"):
        # todo 检查重名
        bank = QuestionBank(bankName, 0)
        list = QuestionBank(listName, 1)
        questions = ExamGeneration._getQuestions(amount,index,model,bank.getQuestions())
        for question in questions:
            print(question)
            list.addQuestion(question)
        # todo 是否需要修改
        list.sort()
        list.saveBank()

    @classmethod
    def _getQuestions(cls,amount, index, model, bankList) -> list:
        questions = []
        if model == 'auto':
            questions = random.sample(bankList,amount)
        else:
            for i in index:
                questions.append(bankList[i])
        return questions

if __name__ == __name__:
    ExamGeneration.generate('科目一','科目一试卷1',20,[])
