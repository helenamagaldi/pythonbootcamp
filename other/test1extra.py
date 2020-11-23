i = 1

while i < 6:
    print (i)
    i = i + 1

    #  output:
    # 1
    # 2
    # 3
    # 4
    # 5

# for is better used for lists - used to read all values within a list

thingies = ["apple", "rock", "dog"]

for x in thingies:
    print(x)

# output:
# 1
# 2
# 3
# 4
# 5
# apple
# rock
# dog

def sayHello(name):
    print("Hello " + name)

insertName = input("Say my name, say my name: ")
sayHello(insertName)