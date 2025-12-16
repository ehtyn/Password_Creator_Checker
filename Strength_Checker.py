from math import sqrt

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


print(int_amt, cap, low, sym)

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
    print(f'difference is {difference}')
    print(f'marginOE is {margin_OE}')
    if difference <= margin_OE:
        password_strength += change_var
    
print(equal_chars)

check_value(equal_chars, int_amt)
check_value(equal_chars, cap)
check_value(equal_chars, low)
check_value(equal_chars, sym)


print(password_strength)