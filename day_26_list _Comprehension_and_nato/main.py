import pandas


data = pandas.read_csv("/Users/sudipto/Documents/code/projects/100days of code/day_26_list _Comprehension_and_nato/nato_phonetic_alphabet.csv")
    
dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict)

word = input("enter a word: ").upper()
output = [dict[letter] for letter in word]
print(output)