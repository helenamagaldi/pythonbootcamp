
arranging things in an Order

F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside braces. The expressions are replaced with their values.


$ x = "hello world"
bash: x: command not found
(base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
$ python3
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = "hello world"
>>> x.replace('l', 'a')
'heaao worad'
>>> x = "hello world"
>>> x[1:4]
'ell'
>>> x[1:5]
'ello'
>>> x[6:11]
'world'
>>> x[-2]
'l'
>>> x[-1]
'd'
>>> x[-3:-1]
'rl'
>>> x[0,6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
>>> x[0:6]
'hello '
>>> x[:6]
'hello '
>>> (shortcut)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'shortcut' is not defined
>>> x = "is" 
>>> y = "my"
>>> z = "name"
>>> c = y + x + z
>>> c
'myisname'
>>> c = y " " + z + x
  File "<stdin>", line 1
    c = y " " + z + x
          ^
SyntaxError: invalid syntax
>>> c = y + " " + z + x
>>> c
'my nameis'
>>> x = "my name is"
>>> x
'my name is'
>>> z = "alex"
>>> y = "my name is {}".format
>>> y
<built-in method format of str object at 0x7fe16ab376f0>
>>> z = input()
hello
>>> z
'hello'
>>> x = 34
>>> y = "alex"
>>> x = "alex"
>>> y = 2
>>> y = "my name is {} 
  File "<stdin>", line 1
    y = "my name is {} 
                      ^
SyntaxError: EOL while scanning string literal
>>> y = "my name is {}
  File "<stdin>", line 1
    y = "my name is {}
                     ^
SyntaxError: EOL while scanning string literal
>>> y = "my name is {}"
>>> y = f"my name is {x}"
>>> y
'my name is alex'
>>> z = f"my name is {x} and my age is {y}" 
>>> z
'my name is alex and my age is my name is alex'
>>> z = f"my name is {y} and my name is {x}"
>>> z
'my name is my name is alex and my name is alex'
>>> x = ["dev", "sports", 342"]
  File "<stdin>", line 1
    x = ["dev", "sports", 342"]
                              ^
SyntaxError: EOL while scanning string literal
>>> x = ["dev", "sports", 342]
>>> z = "my name is {x} and my hobbie  is playing {x} and my age is {x}" 
>>> z
'my name is {x} and my hobbie  is playing {x} and my age is {x}'
>>> z = f"my name is {x} and my hobbie  is playing {x} and my age is {x}" 
>>> z
"my name is ['dev', 'sports', 342] and my hobbie  is playing ['dev', 'sports', 342] and my age is ['dev', 'sports', 342]"
>>> f",u name is {x} and my hobbie is playing {x[1]} and my age is {x[2]}
  File "<stdin>", line 1
    f",u name is {x} and my hobbie is playing {x[1]} and my age is {x[2]}
                                                                        ^
SyntaxError: EOL while scanning string literal
>>> z = f",u name is {x} and my hobbie is playing {x[1]} and my age is {x[2]}
  File "<stdin>", line 1
    z = f",u name is {x} and my hobbie is playing {x[1]} and my age is {x[2]}
                                                                            ^
SyntaxError: EOL while scanning string literal
>>> z = f",u name is {x} and my hobbie is playing {x[1]} and my age is {x[2]}"
>>> z
",u name is ['dev', 'sports', 342] and my hobbie is playing sports and my age is 342"
>>> 
