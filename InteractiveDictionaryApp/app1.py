import json
#creating a variable out of the json data file
data = json.load(open("data.json"))
#function to call definitions from the key value dictionary
#adding a user friendly error message for mispelled words
#the keys are all in lower case to prevent error force the words into lower case
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exsist. Please double check it"

word = input("Enter word: ")

print(translate(word))
