import random
from random import randint

#All uppercase letters
password = ""
for i in range(10):
    i = chr(randint(65,90))
    password = str(password) + i
print(password)

# Version with if statement
password = ""
for i in range(10):
    if i % 2 == 1:
        i = chr(randint(65,90)).lower()
    else:
        i = chr(randint(65,90))
    password = str(password) + i
print(password)

#more efficient version
password = ""
for i in range(5):
    i = chr(randint(65,90))
    j = chr(randint(65,90)).lower()
    password = str(password) + i + j
print(password)

#Version using lists with user input
upper = list(range(65,91))
lower = list(range(97,123))
special = [33, 64, 37, 38, 36]
combined = upper + lower + special
length = input("Please Input the length of characters you want your password to be: ")
length = int(length)
def generator(longth):
    #named the parameter longth because it helps me differentiate the parameter from the actual variable
    password = []
    for i in range(longth):
        password.append(chr(random.choice(combined)))
        #use chr() to find the ASCII character corellating to the int
    return ''.join(password)
    #this returns an empty string joined with every character in the list "password"
    #basically converts our list to a string with all the values concatenated
print(generator(length))
