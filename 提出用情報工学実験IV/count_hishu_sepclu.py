import csv
from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
list = [0] * 20

csv_file = open("DS_hisshu_addclu.csv", "r", encoding="ms932", errors="", newline="" )
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
            list[input_num] += 1

print(list)
y = np.array(list)
x = np.array(range(0,20))
plt.bar(x,y)
plt.show()
