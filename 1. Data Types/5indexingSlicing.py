x.replace is a method, and we need to pass the paramethers using the ()

>>> x = "hello world"
>>> x.replace('l', 'a')
'heaao worad'
>>> 

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
