from math import sqrt
from colorama import Fore, Style, init
init(autoreset = True)

pswd = input('Enter password: ')


int_amt = 0
cap = 0
low = 0
sym = 0

password_strength = 0

for char in pswd:
    try:
        int(char)
        int_amt += 1
    except ValueError:
        pass
    if char.isupper():
        cap += 1
    elif char.islower():
        low += 1
    elif not char.isalnum():
        sym += 1





passwd_len = len(pswd)
if passwd_len < 8:
    change_var = 2
elif 8 <= passwd_len < 16:
    change_var = 6
elif 16 <= passwd_len:
    change_var = 10

equal_chars = passwd_len / 4  # how many instances of a thing there should be
margin_OE = sqrt(equal_chars) # Parameter of error

def check_value(parameter1, parameter2):
    global password_strength
    difference = abs(parameter1 - parameter2)
    if difference < margin_OE:
        password_strength += change_var
    

check_value(equal_chars, int_amt)
check_value(equal_chars, cap)
check_value(equal_chars, low)
check_value(equal_chars, sym)




seen_chars = {} # Creates an empty dictionary of seen characters

for char in pswd:
    if char not in seen_chars: # Checks if the character isnt in seen chars, than if it isnt it adds it with counter of 1
        seen_chars[char] = 1
    else:
        seen_chars[char] += 1 # Adds 1 to the seen counter if counter exists

acceptable_repeats = sqrt(passwd_len)


for value in seen_chars.values():
    if value > acceptable_repeats:
        password_strength -= change_var
    else: 
        password_strength += change_var


max_score = 250

if password_strength >= max_score:
    password_strength = 100
else:
    pass

final_score = password_strength

final_score = min(final_score, 100)

def print_color():
    if 20 >= final_score:
        color = Fore.RED
    elif 40 >= final_score > 20:
        color = Fore.LIGHTRED_EX
    elif 60 >= final_score > 40:
        color = Fore.YELLOW
    elif 80 >= final_score > 60:
        color = Fore.LIGHTGREEN_EX
    elif 100 >= final_score > 80:
        color = Fore.GREEN

    return color

print(print_color() + f'Your password ranked a score of {final_score}%. ')