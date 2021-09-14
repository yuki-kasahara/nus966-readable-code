import sys
import pandas as pd

args = sys.argv 

dictionary = pd.read_csv("dictionary.csv")

# 引数が無ければすべて出力, IDが指定されていれば指定IDの単語出力
if len(args) <= 1:
    for id_, word in zip(dictionary['ID'],dictionary['単語']):
        print(str(id_) + ':' + word)
else:
    print(args[1] + ':' + str(dictionary['単語'][int(args[1])]))