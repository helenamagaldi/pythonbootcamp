k = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in k:
        if i == 6:
            break
        print(i)

number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

words = ["rain", "sun", "moon", "exit", "weather"]
 
for word in words:
        #checking for the breaking condition
        if word == "exit" :
                #if the condition is true, then break the loop
                break;
 
        #Otherwise, print the word
        print (word)

# $ python3 0tests.py 
# 1
# 2
# 3
# 4
# 5
# Number is 0
# Number is 1
# Number is 2
# Number is 3
# Number is 4
# Out of loop
# rain
# sun
# moon