x = 3
y = 3
z = 2

# various elif conditions. various conditions and they are not dependent on them

if(x==y & x==z):
    print("x is equal to y and z")
elif(x == y and x != z):
    print("x is equal to y but not equal to z")
else:
    print("nothing matches, help")

k = 3
l = 3
m = 2

if(k==l | m !=l):
    print("k different l or m equals to l")
else:
    print("nevermind")

