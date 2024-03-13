import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("type a word: ")

result = [data_dic.get(letter.upper()) for letter in user_input]
print(result)