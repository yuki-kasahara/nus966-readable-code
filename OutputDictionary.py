
with open("DictionaryData.txt","r",encoding="utf-8") as dictionary_data:
    dictinary_list = dictionary_data.readlines()
    for word in dictinary_list:
        print(word, end='')