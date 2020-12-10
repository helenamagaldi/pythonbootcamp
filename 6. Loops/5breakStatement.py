x = ["red", "yellow", "green", "pink", "blue", "black"]

for i in x:
    print(i)

# # that way I can print all the elements in the x list.
# $ python3 5.breakStatement.py 
# red
# yellow
# green
# pink
# blue
# black


# # but what if someone doesn't like one particular colour? then will use break. In this case, the program will break after yellow and only show:
# red
# yellow

y = ["red", "yellow", "green", "pink", "blue", "black"]

for i in y:
    print(i)
    if i == "yellow":
        break

# you can also do it with numbers

w = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
# i just need five values
for i in w:
    print(i)
    if i == 6:
        break

# 1
# 2
# 3
# 4
# 5
# 6

# But if I want it to stop before 6, this is the way:
k = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in k:
        if i == 6:
            break
        print(i)


# 1
# 2
# 3
# 4
# 5

# also, if I wanna break the loop before the "yellow" in the first list:

h = ["red", "yellow", "green", "pink", "blue", "black"]

for i in h:
    if i == "yellow":
        break
    print(i)

# red