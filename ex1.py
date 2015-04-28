'''
Exercise 1: "Think Physically"

Classify each line of an input file into animal, vegetable, mineral, or other,
using a set of reference lists; report the counts of each.
'''
from utils import run


# NB: reading the data is supposed to be part of the timing in this exercise.
# Feel free to move or change the code that reads the data, but don't actually
# run anything outside of the "if __name__ == '__main__':" block.

# v Make me faster! v

def reference(filename):
    # Load a reference list
    result = []
    with open(filename) as f:
        for line in f:
            result.append(line.strip())
    return result

def is_animal(s):
    for x in reference('data/ex1-animals.txt'):
        if x == s:
            return True
    return False

def is_vegetable(s):
    for x in reference('data/ex1-vegetables.txt'):
        if x == s:
            return True
    return False

def is_mineral(s):
    for x in reference('data/ex1-minerals.txt'):
        if x == s:
            return True
    return False

def count_things():
    # Prepare the result dictionary
    result = {
        'animals': 0,
        'vegetables': 0,
        'minerals': 0,
        'other': 0
    }

    with open('data/ex1-data.txt') as f:
        # Classify each line
        for line in f:
            # It so happens that the reference lists are mutually exclusive
            if is_animal(line.strip()):
                result['animals'] += 1
            elif is_vegetable(line.strip()):
                result['vegetables'] += 1
            elif is_mineral(line.strip()):
                result['minerals'] += 1
            else:
                result['other'] += 1

    return result

# ^ Make me faster! ^


if __name__ == '__main__':
    expected = {
        'animals': 38079,
        'vegetables': 6149,
        'minerals': 1157,
        'other': 4615
    }
    run(count_things, expected, bronze=5.0, silver=0.5, gold=0.06)
