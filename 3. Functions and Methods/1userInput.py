#  input is a method
 
s = input("first value plz ")
y = input("write the second value plz")
z = s + y
 
print(z)
# s = 2, y = 3 => 23
# in python 3 everything is a string, but in python 2 it would read as an integer and the math would occur. that's not what it happens here (weird, python3)
# in order to do that in python 3 we need to use the casting method:
s = int(s)
y = int(y)
z = s + y
# you can also use: z = int(x) + int(y)

print(z)


# terminal
# /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Funcbash: export: `Fusion.app/Contents/Public:/Users/helenamagaldi/tools': not a valid identifier
# tions and Methods/userInput.py"

# The default interactive shell is now zsh.
# To update your account to use zsh, please run `chsh -s /bin/zsh`.
# For more details, please visit https://support.apple.com/kb/HT208050.
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# 5
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# 11
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz3
# 11
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz 1
# write the second value plz3
# Traceback (most recent call last):
#   File "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py", line 5, in <module>
#     z = x + y
# NameError: name 'x' is not defined
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz 3
# write the second value plz4
# 34
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz 4
# write the second value plz3
# 43
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz 3
# write the second value plz4
# 34
# 34
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# write the second value plz/usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"/usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# Traceback (most recent call last):
#   File "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py", line 11, in <module>
#     s = int(s)
# ValueError: invalid literal for int() with base 10: '/usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"'
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ /usr/local/bin/python3 "/Users/helenamagaldi/Dropbox/Dev/Python Bootcamp 2020/pythonbootcamp/4. Functions and Methods/userInput.py"
# first value plz 4
# write the second value plz3
# 43
# 7
# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in pythonbootcamp
# $ 