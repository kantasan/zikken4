import csv
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
graphname = 'Classted-c4-Elective'
name = 'C-c4-Elective.jpg'
c0 = [0] * 32
c1 = [0] * 32
c2 = [0] * 32
c3 = [0] * 32
c4 = [0] * 32

csv_file = open("DS_senntaku.csv", "r", encoding="ms932", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
#print(header)
for row in f:
    #rowはList
    #row[0]で必要な項目を取得することができる
    if row[-1] == '0':
        for i in range(0,4):
            input_num = int(row[i])
            c0[input_num] += 1
    elif row[-1] == '1':
        for i in range(0,4):
            input_num = int(row[i])
            c1[input_num] += 1
    elif row[-1] == '2':
        for i in range(0,4):
            input_num = int(row[i])
            c2[input_num] += 1
    elif row[-1] == '3':
        for i in range(0,4):
            input_num = int(row[i])
            c3[input_num] += 1
    elif row[-1] == '4':
        for i in range(0,4):
            input_num = int(row[i])
            c4[input_num] += 1


y = np.array(c4)
x = np.array(range(0,32))
plt.bar(x,y)
plt.title(graphname)
plt.savefig(name)
plt.show()
