'''
Exercise 2: "Know Your Language"

Given a list of strings, *without mutating the given list*:
  * Insert "mushroom" after every "badger"; then
  * Replace "mushroom", "snake", and "badger" in an ecological fashion; then
  * Turn the result into a space-separated string.
'''
import gzip
import json
from utils import run


# v Make me faster! v

# This is how ecology works, right?
ECOLOGY = [
    ('mushroom', 'slime mold'),
    ('snake', 'lizard'),
    ('badger', 'ferret')
]

def process_my_list(my_list):
    # We're not allowed to mutate the given list, so make a copy
    my_list = my_list.copy()

    # Add mushrooms
    i = 0
    while i < len(my_list):
        if my_list[i] == 'badger':
            my_list.insert(i + 1, 'mushroom')
            i += 1
        i += 1

    # Apply ecology
    for i in range(len(my_list)):
        for lifeform, kin in ECOLOGY:
            if my_list[i] == lifeform:
                my_list[i] = kin

    # Make the output
    result = ''
    for x in my_list:
        result += x
        result += ' '
    # Trim off the last space if necessary
    if my_list:
        result = result[:-1]
    return result

# ^ Make me faster! ^


if __name__ == '__main__':
    # Load the test data
    with gzip.open('data/ex2-data.json.gz', mode='rt') as f:
        test_data = json.loads(f.read())
    with gzip.open('data/ex2-expected.txt.gz', mode='rt') as f:
        expected = f.read()

    # Define the test function
    def go():
        return process_my_list(test_data)

    # Keep a copy of the test data to check that it wasn't mutated
    test_data_copy = test_data[:]

    # Run the test
    run(go, expected, bronze=1.0, silver=0.15, gold=0.1)

    # Assert that the test data wasn't mutated
    if test_data != test_data_copy:
        raise RuntimeError('Your function mutated the input.')

