# def div(a,b):
#     c = a/b
#     return print(c)

# a = input("enter any value: ")
# b = input("enter the second value: ")

# div(int(a), int(b))

# better yet, since the function above doesn't consider the possibility of b being zero. in that case, the program will return an error

def div(a,b):
    if(b == 0):
        return print("nop, can't do")
    else:
        c = a/b
        return print(c)

a = input("enter any value: ")
b = input("enter the second value: ")

div(int(a), int(b))


# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 7modifyingFuntions.py 
# enter any value: 6
# enter the second value: 3
# 2.0
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 7modifyingFuntions.py 
# enter any value: 6
# enter the second value: 0
# nop, can't do
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ 