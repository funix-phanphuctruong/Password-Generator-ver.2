# Project Generator password
import time
import random
char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','<','>','?','/','|']

print("Welcome to the PyPassword Generator!\n")
time.sleep(1.5)
n_char = int(input("How many letters would you like in your password?\n"))
time.sleep(1.5)
n_num = int(input("How many numbers would you like?\n"))
time.sleep(1.5)
n_sym = int(input("How many symbols would you like?\n"))

passcode = []
password = ""

for i in range(0,n_char):
    passcode.append(random.choice(char))
for i in range(0,n_num):
    passcode += random.choice(num)
for i in range(0,n_sym):
    passcode += random.choice(sym)

random.shuffle(passcode)
for i in passcode:
    password += i

print(f"Your password is: {password}")