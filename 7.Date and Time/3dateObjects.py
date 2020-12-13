import datetime

# if you're not referring to actual time and wanna "create" your own in the project, you use what's called a date object

# instead of using datetime.datime.now() :

x = datetime.datetime(2010, 3, 19)

# if you run this, you'll get the date you're creating:
print(x)

# 2010-03-19 00:00:00 - since i haven't specified the time, it will show 00 hrs

# in this case I can also do 

print(x.day)
print(x.month)
print(x.year)

# 19
# 3
# 2010
