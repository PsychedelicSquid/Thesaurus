import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n": 
            return "The word doesn't exist in the data set. Please check the spelling."
        else:
            return "No comprende."

    else:
        return "The word doesn't exist. Please check the spelling."
    
word = input("Enter Word:")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

