from Repository.MasterList import masterList, addTest
from Controller import masterController, testCreate
from UI.Menu import Menu
addTest()

repo = masterList()
ctrl = masterController(repo)
men = Menu(ctrl)

f = open("masterLine.txt", "r")
line = f.readline()
while (line != ''):
    params = line.split(";")
    ctrl.add(params)
    line = f.readline()
testCreate()

#print(repo)
men.start()