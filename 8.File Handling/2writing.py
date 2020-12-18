# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 8.File Handling
# $ python3
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = open("ex2.txt", "r"
# ... )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'ex2.txt'
# >>> x = open("ex2.txt", "w")
# >>> file.close()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'file' is not defined
# >>> x.close()
# >>> x = open("ex2.txt", "w")
# >>> x.write("pink")
# 4
# >>> x.write("pink  ")
# 6
# >>> 

# if i open and write in the terminal, it wont be in the file until i close it. when I try to read a file that doesn't exist, I'll get an error - if a write it, it will create one. in the above example, I tried putting pink and the output was the number of characters I've tried to insert. this information will only go to the file after I close it

# but if i add something new to the file the oldest part will be replaced. if i have pink, black, yellow and add pink with x.write("pink"), everything will be replaced by just pink

# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 8.File Handling
# $ python3
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = open("ex2.txt", "r"
# ... )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'ex2.txt'
# >>> x = open("ex2.txt", "w")
# >>> file.close()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'file' is not defined
# >>> x.close()
# >>> x = open("ex2.txt", "w")
# >>> x.write("pink")
# 4
# >>> x.write("pink  ")
# 6
# >>> x.close()
# >>> file = open("tes.txt", "w")
# >>> file.write("pink")
# 4
# >>> file.write("white/m")
# 7
# >>> file.close()
# >>> file = open("tes.txt", "w")
# >>> file.write("white\n")
# 6
# >>> file.close()
# >>> file = open("tes.txt", "w")
# >>> file.write("pink\n")
# 5
# >>> file.close()
# >>> x = ["red", "pink", "black", "blue"]
# >>> file = open("tes.txt", "w")
# >>> for item in x:
# ...     file.write(item + "\n")
# ... file.close()
#   File "<stdin>", line 3
#     file.close()
#     ^
# SyntaxError: invalid syntax
# >>> file = open("tes.txt", "w")
# >>> for item in x:
# ...     file.close()
# ...     file.write(item + "\n")
# ... QUIT()
#   File "<stdin>", line 4
#     QUIT()
#     ^
# SyntaxError: invalid syntax
# >>> file = open("tes.txt", "w")
# >>> file.wirte("pink")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: '_io.TextIOWrapper' object has no attribute 'wirte'
# >>> file.write("pink")
# 4
# >>> file.close()
# >>> file = open("tes.txt", "w")
# >>> file.write("white")
# 5
# >>> file = open("tes.txt", "w")
# >>> file.write("pink\n")
# 5
# >>> file.write("black\n")
# 6
# >>> file.close()
# >>> x = ["red", "blue", "pink", "black"]
# >>> file = open("tes.txt", "w")
# >>> x = ["red", "blue", "pink", "black"]
# >>> for item in x:
# ... file.write(item+ "\n")
#   File "<stdin>", line 2
#     file.write(item+ "\n")
#     ^
# IndentationError: expected an indented block
# >>> for item in x:
# ...     file.write(item + "\n")
# ... file.close()
#   File "<stdin>", line 3
#     file.close()
#     ^
# SyntaxError: invalid syntax
# >>> file.write(item+ "\n")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'item' is not defined
# >>> file = open("tes.txt", "w")
# >>> for item in x:
# ...     file.write(item + "\n")
# ... 
# 4
# 5
# 5
# 6
# >>> file.close()
# >>> 