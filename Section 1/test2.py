

print(tchoTcho)

# output
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# ['hey', 'ho', "let's", 'go']
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# ['hey', 'ho', "let's", 'go']
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# ['hey', 'ho', "let's", 'go']
# let's
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# ['hey', 'ho', "let's", 'go']
# go
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ 

def lets_go():
    letters = len(tchoTcho)
    print(letters)

# lets_go()

def bye(badName):
    print("hasta la vista " + badName)

bye("very bad name")

def hello(name):
    print("WELL, HELLO THERE " + name)

hello("hell")

# output
# base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1
# $ python3 test2.py 
# ['hey', 'ho', "let's", 'go']
# go
# hasta la vista very bad name
# WELL, HELLO THERE hell
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in Section 1

#  if i really want an string: wont accept other kinds of variables or its going to try to transform it into a str
def blabla(tchu = str):
    print("bla bla bla" + tchu)


