import os


def run(path):
    dst = path.split(".")[0] + ".py"
    os.system("D:\\anaconda3\\python.exe -m PyQt5.uic.pyuic " + path + " -o " + dst)


def getDir(basedir):
    nms = os.listdir(basedir)

    for nm in nms:
        path = os.path.join(basedir, nm)
        if os.path.isdir(path):
            getDir(path)
        else:
            if nm.split(".")[1] == "ui":
                run(path)


# 只是偷懒方便编译ui文件的一个小脚本
dir = "E:\\coding\\python\\homework\\Online-question-bank-platform\\ui"

getDir(dir)
