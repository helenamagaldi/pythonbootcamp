# https://stackabuse.com/how-to-format-dates-in-python/ it varies a lot, just check the lst to know exactly what you need to write to get what you want

import datetime

x = datetime.datetime.now()
# string formatting time

print(x.strftime("%p"))
# PM

print(x.strftime("%w"))
# 0




