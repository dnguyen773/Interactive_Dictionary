import json
import difflib
#!/usr/bin/env python
#Change this to the directory of where data.json is located
data = json.load(open("/Users/dannynguyen/PycharmProjects/files/data.json"))

def word_finder(w):
    if w in data:
        return data[w]
    elif len(difflib.get_close_matches(w,data.keys()))> 0:
        user_input = input("Did you mean %s instead? Enter N or Y "% difflib.get_close_matches(w,data.keys())[0])
        if user_input.upper() =="Y":
             return data[difflib.get_close_matches(w,data.keys())[0]]
        elif user_input.upper() =="N":
            return "Sorry, the word doesn't exist. Please double check it"
        else:
            return "Sorry but we don't understand your entry.."
    else:
        return "The word doesn't exist"


print("Welcome to the English Dictionary!")
while True:
    word = input("Enter a word you would like to look up.\n ")
    if word == "stop":
        break
    else:

        # print(word_finder(word))
        output = word_finder(word.lower())
        if type(output) == list:
            increment = 1
            for item in output:
                print(increment, ":" , item)
                increment += 1
        else:
            print(output)
