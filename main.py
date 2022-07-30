import sys

from ui import WindowController
from PyQt5.QtWidgets import QApplication
from question.QuestionBank import QuestionBank
from question.Question import Question
from function.ExamGeneration import ExamGeneration

INDEX_FILE = open('./data/INDEX.txt','w+')
INDEX = INDEX_FILE.readline()
INDEX = 1 if len(INDEX) == 0 else int(INDEX)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # window = MyReviseLoadFile.MyReviseLoadFile(mainWindow)
    # mainWindow.show()
    # controller= WindowController.WindowController()
    # sys.exit(app.exec_())
    # bank = QuestionBank("科目一", 0)
    # for i in range(150):
    #     bank.addQuestion(Question(INDEX, chr(i + ord('a')), i%3 + 1, 'bad', 'cc', ['a', 'b', 'c']))
    #     INDEX += 1
    # bank.saveBank()
    ExamGeneration.generate('科目一','科目一试卷1',20,[])
    INDEX_FILE.write(str(INDEX))
    INDEX_FILE.close()