# import random
# # declare a variable
# def shuffle(string):
#     tempList = list(string)
#     random.shuffle(tempList)
#     return ''.join(tempList)

# #Main program start here
# uppercaseLatter1 = chr(random.randint(65,90)) #generate a random uppercase laeetr(based on ASCII code)
# uppercaseLatter2 = chr(random.randint(65,90)) #Generate a random uppercase letter(based on ASCII code)

# #Generate more character here
# #...

# #Generate password using all the characters, in random order
# password = uppercaseLatter1+uppercaseLatter2
# password = shuffle(password)
# for p in uppercaseLatter1:
#     if len(p) <200:
#         print(p)


# #Output
# print(password)



import random
import secrets
import string

#define the alphabets
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters+digits+special_chars

#Fix password length
pwd_length = 12

#Generate password string
pwd = ''
for i in range(pwd_length):
    pwd+= ''.join(secrets.choice(alphabet))

print(pwd)

#Generate password meeting contrains
while True:
    pwd = ''
    for i in range(pwd_length):
        pwd+= ''.join(secrets.choice(alphabet))

    if(any(char in special_chars for char in pwd) and sum (char in digits for char in pwd)>=2):
        break
print(pwd)