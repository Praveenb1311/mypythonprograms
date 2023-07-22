import random
import math
import string

letter = string.ascii_lowercase
number = string.digits
special_letter = "@#$%&"  # if requrird we can use as string.punctuation
#find the password length with out user
#password_length = random.randint(8,13)
password_length = int(input("Please enter the password length: "))
letters_length = password_length//2
number_length = math.ceil(password_length*30/100)
special_letter_length = password_length -(letters_length + number_length)

print(password_length)
print(number_length)
print(letters_length)

password = []

def generate_password(length, array, is_letter = False):
    for i in range(length):
        index = random.randint(0, len(array)-1)
        character = array[index]

        if is_letter:
            var = random.randint(0,1)
            if var == 1:
                character = character.upper()
        password.append(character)


generate_password(letters_length, letter, True)
generate_password(number_length, number)
generate_password(special_letter_length,special_letter)
random.shuffle(password)
print(password)
new_generated_password = ""
for j in password:
    new_generated_password += str(j)
print(new_generated_password)
