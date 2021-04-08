import json
from posix import ST_MANDLOCK

data = json.load(open("data.json"))

# print(data["smog"])
def translate(word):
    if word in data:
        return data[word]
    else:
        return None        

word = input("Enter the word you'd like to search: ")
output = translate(word)
print(output)