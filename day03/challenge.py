#https://adventofcode.com/2022/day/3

file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]

#Part 1
"""
Every line is a rucksack with a list of items in it.
Every rucksack has two compartments
the first half of the string is the first compartment
the second half of the string is the second compartment

The challenge is to find the items that are in both compartments and score them

Scoring:
Lowercase:
a: 1 point
b: 2 points
c: 3 points
...
x: 24 points
y: 25 points
z: 26 points

Uppercase:
A: 27 points
B: 28 points
C: 29 points
...
X: 50 points
Y: 51 points
Z: 52 points
"""

def score(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

def get_items(line):
    first_half = line[0][:len(line[0])//2]
    second_half = line[0][len(line[0])//2:]
    return first_half, second_half

def part1():
    total = 0
    for line in lines:
        first_half, second_half = get_items(line)
        addedChars = []
        for item in first_half:
            if item in second_half:
                if item not in addedChars:
                    total += score(item)
                    addedChars.append(item)
    return total

print("Part 1:", part1())

#Part 2
"""
3 lines is one group of rucksacks for three elves
each group has a badge, that is the same for all three rucksacks but has an error in it so
it has to be removed

The challenge is to find the items that are in all three compartments and score them
each group may have a different item in the badge

Scoring:
Lowercase:
a: 1 point
b: 2 points
c: 3 points
...
x: 24 points
y: 25 points
z: 26 points

Uppercase:
A: 27 points
B: 28 points
C: 29 points
...
X: 50 points
Y: 51 points
Z: 52 points
"""

def part2():
    total = 0
    for i in range(0, len(lines), 3):
        first_line = lines[i]
        second_line = lines[i+1]
        third_line = lines[i+2]
        addedChars = []
        for item in first_line[0]:
            if item in second_line[0] and item in third_line[0]:
                if item not in addedChars:
                    total += score(item)
                    addedChars.append(item)
    return total

print("Part 2:", part2())