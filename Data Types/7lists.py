# we can store different types of data in lists, but it always have to be between [] 

# dir(list) = you can get all the elements in the list 

# x[2] = you can acess the elements like we did back there with indexes

# remove the last: x.pop()

# if you wanna add: x.append

# if i wanna remove another item: x.remove["yellow"]

# if you wanna delete the whole list: del.x

(base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
$ python3
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = "helena
  File "<stdin>", line 1
    x = "helena
              ^
SyntaxError: EOL while scanning string literal
>>> x = "string"
>>> x
'string'
>>> x = [1, 2, 3, 4]
>>> x
[1, 2, 3, 4]
>>> x = 234
>>> x
234
>>> x = ["red", "blue", "green", "yellow", "black"]
>>> x
['red', 'blue', 'green', 'yellow', 'black']
>>> x = ["red", "blue", "green", "yellow", "black", 3]
>>> x
['red', 'blue', 'green', 'yellow', 'black', 3]
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> x[2]
'green'
>>> x[-2]
'black'
>>> 2[-1]
<stdin>:1: SyntaxWarning: 'int' object is not subscriptable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> x[-1]
3
>>> x.lenght
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'lenght'
>>> x.length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'length'
>>> len(x)
6
>>> x.pop()
3
>>> x
['red', 'blue', 'green', 'yellow', 'black']
>>> x.append()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (0 given)
>>> x.append(9)
>>> x
['red', 'blue', 'green', 'yellow', 'black', 9]
>>> x.remove("yellow
  File "<stdin>", line 1
    x.remove("yellow
                   ^
SyntaxError: EOL while scanning string literal
>>> x.remove("yellow")
>>> z
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> x
['red', 'blue', 'green', 'black', 9]
>>> del.x
  File "<stdin>", line 1
    del.x
       ^
SyntaxError: invalid syntax
>>> del.x()
  File "<stdin>", line 1
    del.x()
       ^
SyntaxError: invalid syntax
>>> del x
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> 