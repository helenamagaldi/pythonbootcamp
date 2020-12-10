##### ATTRIBUTE ERROR #$####
# # # if you try to implement a method that is incomplatible with the variable


# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ python3
# Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> dir("string")
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> x = 
#   File "<stdin>", line 1
#     x = 
#        ^
# SyntaxError: invalid syntax
# >>> x = "deck"
# >>> y = 23
# >>> x.title()
# 'Deck'
# >>> y.title()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'title'
# >>> 


##### RUNTIME ERROR #####
# raised when an error does not fall under any other cathegory