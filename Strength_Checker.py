from math import sqrt
from colorama import Fore, Style, init
init(autoreset = True)

# Password strength tester. Prints output in a colored way.
# This checker values length and entropy. The shorter a password is, the more strict it is on entropy
def main(pswd):



    int_amt = 0 # Integer amount in password
    cap = 0 # Capital letter amount in password
    low = 0 # Lowercase amount in password
    sym = 0 # Symbol amount in password

    password_strength = 0

    if len(pswd) == 0:
        final_score = 0
        return final_score

    # Checks each char systematically
    # Methodical checking stage
    try:
        for char in pswd:
            if char.isdigit(): # More efficient way of checking if char is number than try/except
                int_amt += 1
            elif char.isupper():
                cap += 1
            elif char.islower():
                low += 1
            elif not char.isalnum():
                sym += 1
            else:
                print(Fore.RED + f'Character {char} was not identifiable. ')
                break
    except Exception as e:
        print(f'The program ran into error {e}. ')
        pass

    # End methodical checking stage

    # Adds variable points based on length of password
    # Variable points system
    passwd_len = len(pswd)
    if passwd_len < 8:
        change_var = 2
    elif 8 <= passwd_len < 16:
        change_var = 6
    elif 16 <= passwd_len:
        change_var = 10
    # End variable points system

    equal_chars = passwd_len / 4  # how many instances of a character type there should be
    margin_OE = sqrt(equal_chars) # Parameter of error

    def check_value(parameter1, parameter2):
        difference = abs(parameter1 - parameter2)
        if difference < margin_OE:
            return change_var
        else: # Makes the checker more strict 
            return change_var
        

    password_strength += check_value(equal_chars, int_amt)
    password_strength += check_value(equal_chars, cap)
    password_strength += check_value(equal_chars, low)
    password_strength += check_value(equal_chars, sym)


    seen_chars = {} # Creates an empty dictionary of seen characters

    # Dictionary updater
    for char in pswd:
        if char not in seen_chars: # Checks if the character isnt in seen chars, than if it isnt it adds it with counter of 1
            seen_chars[char] = 1
        else:
            seen_chars[char] += 1 # Adds 1 to the seen counter if counter exists
    # End dictionary updater

    acceptable_repeats = margin_OE


    # This line is lowkey tuff ngl 

    # Character repeat checker
    for value in seen_chars.values():
        if value > acceptable_repeats: # Checks if there are more instances of a char than acceptable. If so, it subtracts the change_var from score.
            password_strength -= change_var
        else: 
            password_strength += change_var
    # End character repeat checker

    # Strength limiter
    max_score = 100

    if password_strength >= max_score:
        password_strength = 100
    elif password_strength <= 0:
        password_strength = 0
    else:
        pass
    # End strength limiter

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
    if __name__ == '__main__':
        print(print_color() + f'Your password ranked a score of {final_score}%. ')
    else:
        return final_score

if __name__ == '__main__':
    main(input('Enter password to test. '))
else:
    pass