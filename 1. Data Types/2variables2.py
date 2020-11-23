# int and float are both the same things: numbers 

 # arithmetic operators
#  + - * / **(power operator) ()[not math operators, but obviously very useful when it comes to mathematical functionsz]


x = (3 + 5) * 6
#  obviously different from 3 + 5 * 6 // remember that some operators have priority on operations

print(x)

y = 3 + 5 * 6

print(y)

z = 3 + 5 * 2 ** 2 / 16 - 1
#  left to right precedency
#  3 + 20 / 16 - 1 // but here it will make the / first because: precedency 
#  3 + 1.25 - 1

z1 = ((3 + 5) * 2) ** 2 / 16 - 1 

# divide is below power operator

print(z)
print(z1)