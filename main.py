import json

data = json.load(open("data.json"))


def lookup(word):
    if word not in data:
        return "Word not in thesaurus!"
    return data[word][0]


word = input("Enter word: ")

print(lookup(word))
