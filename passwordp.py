import random
import string

print('Welcome to Password Picker!')

while True:
    specialChar = '#'
    number = random.randrange(100, 400)
    specialChar1 = '*'
    number1 = random.randrange(400, 500)
    specialChar2 = random.choice(string.punctuation)
    number2 = random.randrange(500, 900)
    
    password = specialChar + str(number) + specialChar1 + str(number1) + specialChar2 + str(number2)
    print('Your new password is: %s' % password)
    
    response = input('Would you like another password? Type y or n:')
    if response == 'n':
        break
