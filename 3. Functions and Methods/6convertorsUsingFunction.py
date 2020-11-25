def fahrenheit(a):
    z = int(a)
    z = (9/5)*a + 32
    return print(int(z))

def time(m,s):
    h = int(m) / 60 + int(s) / 3600
    return print(h)

c = input("enter the temperature in celsius")
c = int(c)

fahrenheit(c)

m = input("enter the number of minutes")
s = input("enter the number of seconds")

time(m,s)

# I WROTE THIS ALL BY MYSELFFFFFF

# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ python3 6convertorsUsingFunction.py 
# enter the temperature in celsius45
# 113
# enter the number of minutes45
# enter the number of seconds6000
# 2.416666666666667
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 3. Functions and Methods
# $ 
