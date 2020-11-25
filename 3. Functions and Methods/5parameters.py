def add( x , y = 0 ):
    z = x + y
    return print(z)

    # function above doesn't depend on the numbers we'll use

# redefining the parameters
a = input("write the first number: ")
b = input("write the second number: ")
a = int(a)
b = int(b)

# if you put only a before defining a default value, you'll get an error. 
add(a)

# how to get around that? you'll need to define the default value for y:
# def add(x, y = 0): # that way it will work because it doesn't matter what will be tiped, you already have a default value

# by then you can also ignore letter be and just make one input and the function will also work


# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 5parameters.py 
# write the first number: 3
# write the second number: 4
# 3
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ 




