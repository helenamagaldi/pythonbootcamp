# from _typeshed import NoneType


# identity operators
# 1. is (equal or not)
# 2. is not

# membership operators****
# 1. in
# 2. not in

(base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
$ python3
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 3 > 2 and 4 > 2
True
>>> 2 > 2 and 4 > 2
False
>>> 3 > 2 and 4 > 2 and 2 > 1
True
>>> 2>2 and 4 > 2 and 2 > 1
False
>>> 3 > 2 or 4 > 2
True
>>> 3 < 2 or 4 > 2
True
>>> 2 < 2 and 4 < 2
False
>>> 2 < 2 or 4 < 2
False
>>> 3 > 2
True
>>> not 3 > 2
False
>>> not 3 > 2
False
>>> not 3 < 2
True
>>> x = 3
>>> y = 3
>>> x is y
True
>>> z = 5
>>> z is x
False
>>> x is not z
True
>>> x = [1, 2, 3, 4]
>>> 3 in x
True
>>> 6 in x
False
>>> 5 in x
False
>>> 3 not in x
False
>>> 9 not in x
True
>>> x= "water is life" 
>>> e in x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e' is not defined
>>> "e" in x
True
>>> "z" in x
False
>>> "z" not in x
True
>>> 