from matplotlib import pyplot
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
"""
listsは必修科目、list2は選択科目。
それぞれ0番目からAさん,Bさん...みたいな形式を取ること！
文字を数値に置き換える.例えばos 0 コンシス 1とか
"""
#授業の数
n = 34
graphname = 'group-0 Elective'
name = 'c0-Elective.jpg'

list_in = []
kamoku_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

print("0 キャリア実践\n" +
"1 大学英語\n" +
"2 情報社会と情報倫理\n" +
"3 モデリングと設計\n" +
"4 プロジェクト・デザインII\n" +
"5 情報工学実験III,IV\n" +
"6 ソフトウェア演習I,II\n" +
"7 プログラミングI,II\n" +
"8 情報工学実験I,II\n" +
"9 アルゴリズムとデータ構造\n" +
"10 情報ネットワークI\n" +
"11 オペレーティングシステム\n" +
"12 データベースシステム\n" +
"13 コンピュータシステム\n" +
"14 計算機アーキテクチャ\n" +
"15 線型代数学\n" +
"16 情報数学I,II\n" +
"17 数学基礎演習I,II\n" +
"18 微分積分I,II\n" +
"19 物理I,II\n" +
"20 確率及び統計\n")

while len(list_in) != 5:
    x = input("好きだった科目の番号を入力してください:")
    if (x in list_in):
        print("まだ入力していない科目を選んでください。")
    elif (not x in kamoku_list):
        print("0~23までの数字のみ入力してください。")
    else:
        list_in.append(int(x))

#print(list_in)


lists = []
list2 = []
file_name = "DS_hisshu.csv"
file_name2 = "DS_senntaku.csv"

csv_file = open(file_name, "r", encoding="ms932", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)

for row in f:
    list_test = []
    for s in range(0,5):
        list_test.append(int(row[s]))
    lists.append(list_test)
"""
try:
    file = open(file_name)
    lines = file.readlines()
    count = 0
    test = []
    for line in lines:
        test.append(line.strip())
        count = count + 1
        if count == 5:
            lists.append(test)
            count = 0
            test = []
    #print(lists)
except Exception as e:
    print(e)
finally:
    file.close()
list2 = []
try:
    file = open(file_name2)
    lines2 = file.readlines()
    count2 = 0
    test2 = []
    for line in lines2:
        test2.append(int(line.strip()))
        count2 = count2 + 1
        if count2 == 5:
            list2.append(test2)
            count2 = 0
            test2 = []
    #print(list2)
except Exception as e:
    print(e)
finally:
    file.close()
"""
csv_file = open(file_name2, "r", encoding="ms932", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

for row in f:
    list_test2 = []
    for s in range(0,5):
        list_test2.append(int(row[s]))
    list2.append(list_test2)



#必修->ファイル読み込み
#lists =[[1,2,3,4,5],[4,5,6,7,8]]
sets = list(map(lambda x: set(x),lists))
print(sets)
#選択これも
#list2 = [[11,10,9,12,13],[11,15,16,23,24]]
set2 = list(map(lambda x: set(x),list2))
print(set2)

match_index = []
#入力


#list_in = [1,2,3,4,5]
set_in = set(list_in)
print(set_in)
"""
listsの中から１つ以上一致する人を探してindexをmatch_indexに保存
list2[match_index[i]]とかで必修を選んだ人の選択科目がわかる。
マッチしたのが1以上とかなり雑なため、マッチした数に重みを与える必要がある。
"""
for i in range(len(sets)):
    print(len(sets[i] & set_in))
    if len(sets[i] & set_in) >= 1:
        match_index.append(i)

print(match_index)
#print(list2[match_index[0]])

recomend = [0]*n
print(recomend)
"""
マッチした人の選択科目をカウントして多いものから順にとって出力。
recomendのindexは数値化した授業に対応している。
重みをつけるならrecomendのところ
"""

for k in match_index:
    for j in range(5):
        recomend[list2[k][j]] += 1 * len(sets[k]&set_in)/5

print(recomend)
print(recomend.index(max(recomend)))

plt.title(graphname)
y = np.array(recomend)
x = np.array(range(0,n))
plt.bar(x,y)
plt.savefig(name)
plt.show()
