# # append will also create a new file 

# (base) helenamagaldi@MacBook-Pro-de-Helena-2 in 8.File Handling
# $ python3
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39) 
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> file = open("test2.txt", "a")
# >>> file.write("pink")
# 4
# >>> file.close()
# >>> file = open("test2.txt", "a")
# >>> file.write("pink")
# 4
# >>> file.close()
# >>> file = open("tess.txt", "a")
# >>> file.write("heavy")
# 5
# >>> file.close()
# >>> file = open("tess.txt", "a")
# >>> file.wirte("medium weight")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: '_io.TextIOWrapper' object has no attribute 'wirte'
# >>> file.write("medium weight")
# 13
# >>> file.close()
# >>> 