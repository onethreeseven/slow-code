'''
Exercise 3: "A Bright Idea"

Finds the smallest positive number that:
  * Is an even length palindrome when written in base 10
  * Contains the string "abc" when written in base 16
'''
from utils import run


# v Make me faster! v

def is_even_length_palindrome(n):
    # Write the number in base 10
    s = str(n)

    # Is it not even length?
    if len(s) % 2 != 0:
        return False

    # Is it not a palindrome?
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False

    # Okay, it passes
    return True

def has_abc(n):
    # Write the number in base 16 and search for the test string
    if 'abc' in hex(n):
        return True
    return False

def find_my_number():
    # Go through the numbers in increasing order until one passes
    n = 1
    while True:
        if is_even_length_palindrome(n) and has_abc(n):
            return n
        n += 1

# ^ Make me faster! ^


if __name__ == '__main__':
    # The timings here illustrate a surprisingly common feature of "simple"
    # performance problems: incremental fixes can get you small improvements,
    # but having a bright idea can get you multiple orders of magnitude
    run(find_my_number, 883388, bronze=0.5, silver=0.2, gold=0.002)
