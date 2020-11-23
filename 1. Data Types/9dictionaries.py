# we use the keys
# x = {"number":1}
# first is the key, after that it's the value attributed to that key

# things after the comma are components. 
# dictionaries are manipulated - but we need to inform the parameter 

(base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
$ python3
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = {"number":1}
>>> x = {"number":1, "name":"blue","age": 200}
>>> x
{'number': 1, 'name': 'blue', 'age': 200}
>>> x["name"]
'blue'
>>> x["age"] 
200
>>> x["age"] = 300
>>> x
{'number': 1, 'name': 'blue', 'age': 300}
>>> x["name"] = "alex" 
>>> len(x)
3
>>> x["year"] = 2020
>>> x
{'number': 1, 'name': 'alex', 'age': 300, 'year': 2020}
>>> x.pop("number")
1
>>> x
{'name': 'alex', 'age': 300, 'year': 2020}
>>> x.popitem()
('year', 2020)
>>> x
{'name': 'alex', 'age': 300}
>>> 
