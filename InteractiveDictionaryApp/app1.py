import json
from difflib import get_close_matches
#using get_close_matches as an algorithm to check for mispelled words
#creating a variable out of the json data file
data = json.load(open("data.json"))
#function to call definitions from the key value dictionary
#adding a user friendly error message for mispelled words
#the keys are all in lower case to prevent error force the words into lower case
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
#if the value is false > 0 the conditional will move to the last condition
#if it is mispelled use algorithm to find similar words and store as a variable
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. CASE SENSITIVE: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesnt exsist. Please double check it."
        else:
            return "I didnt understand your entry"
    else:
        return "The word doesn't exsist. Please double check it"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
