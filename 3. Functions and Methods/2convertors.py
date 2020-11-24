# transforming celsius to fahrenheit

# c = input("state your temperature")
# f = (9/5)*c + 32 if we use this we'll get a error. In this case, I haven't converted c into into an integer
#error:
# $ python3 2convertors.py 
# state your temperature3
# Traceback (most recent call last):
#   File "2convertors.py", line 4, in <module>
#     f = (9/5)*c + 32
# TypeError: can't multiply sequence by non-int of type 'float'





c = input("state your temperature")
c = int(c)
f = (9/5)*c + 32


print(f)
# can also use:
#  print(int(f))


m = input("enter the number of minutes")
s = input("enter the number of seconds")
h = int(m)/60 + int(s)/3600

print(h)