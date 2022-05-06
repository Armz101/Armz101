import random

print('Welcome to the password generator')

chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'

number = 1


length = int(input('Input your password length: '))

print("Here is your password: ")

def createpas():
    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords = passwords + random.choice(chars)
    return passwords

while True:
    print(createpas())
    anotherpass = input('Would you like to create another password? (Y/N) ')
    if anotherpass.upper() != "Y":
        break