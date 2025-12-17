import random

def select_random_char():
        choice = None
        item = 'abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+=-`[]{}"|;.:>/,?<"'
        choice = random.choice(item)
        return choice

def main():
    select_random_char()

if __name__ == '__main__':
    main()