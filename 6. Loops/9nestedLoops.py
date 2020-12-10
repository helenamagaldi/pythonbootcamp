# loop inside a loop

# x = ["helena", "magaldi", "patricia", "gusmão"]
# y = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

# for i in x:
#     for a in y:
#         print(x,y) 

# $ python3 9nestedLoops.py 
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']
# ['helena', 'magaldi', 'patricia', 'gusmão'] ['frederico', 'francisco', 'bilbo', 'thorin', 'francisca']

# what happened, jeeeesus?
# it will print each and every one of the itens in the first list to the second one.
# if i do this:



k = ["helena", "magaldi", "patricia", "gusmão"]
l = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

for i in k:
    for m in l:i = "helena"
    print(k,l) 
# then this will only print it 5 times, one for each of the l items list

# if i wanna print it item by item: use index. I'm transforming the items in indexes:
# d = ["helena", "magaldi", "patricia", "gusmão", "tamires"]
# e = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

# a = 0
# b = 0

# for i in d: 
#     for f in e:
#         print(d[a],e[b]) 
#         b += 1
#     a += 1

# # we'll get this:
# helena frederico
# helena francisco
# helena bilbo
# helena thorin
# helena francisca
# Traceback (most recent call last):
#   File "9nestedLoops.py", line 55, in <module>
#     print(d[a],e[b]) 
# IndexError: list index out of range

m = ["helena", "magaldi", "patricia", "gusmão", "tamires"]
n = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

o = 0
p = 0

for i in m: 
    for r in n:
        print(m[0],n[4]) 
        o += 1
    p += 1

# # output:
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca
# helena francisca

m_1 = ["helena", "magaldi", "patricia", "gusmão", "tamires"]
n_1 = ["frederico", "francisco", "bilbo", "thorin", "francisca"]

o_1 = 0
p_1 = 0

for i in m_1: 
    for r_1 in n_1:
        print(m_1[o_1],n_1[p_1]) 
        p_1 += 1
    o_1 += 1
    p_1 = 0 

# helena frederico
# helena francisco
# helena bilbo
# helena thorin
# helena francisca
# magaldi frederico
# magaldi francisco
# magaldi bilbo
# magaldi thorin
# magaldi francisca
# patricia frederico
# patricia francisco
# patricia bilbo
# patricia thorin
# patricia francisca
# gusmão frederico
# gusmão francisco
# gusmão bilbo
# gusmão thorin
# gusmão francisca
# tamires frederico
# tamires francisco
# tamires bilbo
# tamires thorin
# tamires francisca