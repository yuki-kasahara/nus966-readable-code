import pandas as pd

dictionary = pd.read_csv("dictionary.csv")

for id_, word in zip(dictionary['ID'],dictionary['単語']):
    print(str(id_) + ':' + word)