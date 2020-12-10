# what if I just want the yellow?

h = ["red", "yellow", "green", "pink", "blue", "black"]

for i in h:
    if i == "yellow":
        continue
    print(i)


# $ python3 6.continueStatement.py 
# red
# green
# pink
# blue
# black

# it also works with numbers
x = [1, 2, 3, 4, 5, 6, 7, 8]

for i in x:
    if i == 5:
        continue
    print(i)


# 1
# 2
# 3
# 4
# 6
# 7
# 8

