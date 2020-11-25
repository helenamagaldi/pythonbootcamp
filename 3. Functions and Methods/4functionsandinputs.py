def add(x,y):
    z = x + y 
    return print(z)

a = input("enter the first value: ")
b = input("enter the second value: ")
# REMEMBER that here the number will be considered as a string. in this case, we have to convert it into an integer, or else we'll have 34 as the return instead of 7
a = int(a)
b = int(b)
add(a,b)

# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 4functionsandinputs.py 
# enter the first value: 3
# enter the second value: 4
# 34
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 4functionsandinputs.py 
# enter the first value: 3
# enter the second value: 4
# 7
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ 