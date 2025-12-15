pswd = input('Enter password: ')

char_amt = 0
int_amt = 0
cap = 0
low = 0
sym = 0

for char in pswd:
    try:
        int(char)
        int_amt += 1
    except ValueError:
        if char.isalpha():
            char_amt += 1
    if char.isupper():
        cap += 1
    elif char.islower():
        low += 1
    elif not char.isalnum():
        sym += 1


print(char_amt, int_amt, cap, low, sym)
passwd_len = len(pswd)
val = passwd_len / 5
