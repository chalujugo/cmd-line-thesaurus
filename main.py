import json

data = json.load(open("data.json"))


def lookup(word):
    return data[word][0]


word = input("Enter word: ")

print(lookup(word))
