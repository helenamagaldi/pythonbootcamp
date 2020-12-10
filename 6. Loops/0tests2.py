x = ["helena", "magaldi", "patricia", "gusmão", "tamires"]
y = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

a = 0
b = 0

for i in x: 
    for k in y:
        print(x[a],y[b])
        b += 1
    a += 1
    b = 0 