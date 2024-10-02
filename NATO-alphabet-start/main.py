
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas
#data = pandas.read_csv("nato_phonetic_alphabet.csv", usecols=["letter", "code"])
#data_dict = data.to_dict(orient="records")
#data_frame = pandas.DataFrame(data_dict)

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

#bravo_words = []
#for letter in word:
#    for (index, row) in phonetic_dict.items():
#        if row.letter == letter:
#            bravo_words.append(row.code)

#print(bravo_words)