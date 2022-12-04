#https://adventofcode.com/2022/day/4

file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]

# Part 1
"""
Each line represents a pair of elves who each get a section to clean.
but they can only clean the section they are assigned
the thing is that in some pairs one of the sections is a subset of the other

the challenge is to find the number of pairs that have completely overlapping sections so not ones that overlap by a few but those were the first one is for example 3-9 and the second is 5-7
so the second one is contained in the first one

the elves in the pairs are seperated by a comma
"""

def is_subset(from1, to1, from2, to2):
    if from1 <= from2 and to1 >= to2:
        return True
    return False

def part1():
    count = 0
    for line in lines:
        elves = line[0].split(",")
        elf1 = elves[0]
        elf2 = elves[1]
        from1 = int(elf1.split("-")[0])
        to1 = int(elf1.split("-")[1])
        from2 = int(elf2.split("-")[0])
        to2 = int(elf2.split("-")[1])
        if is_subset(from1, to1, from2, to2) or is_subset(from2, to2, from1, to1):
            count += 1
    return count

print("Part 1:", part1())

# Part 2
"""
Each line represents a pair of elves who each get a section to clean.
but they can only clean the section they are assigned
the thing is that in some pairs one of the sections overlap

the challenge is to find the number of pairs that have overlapping sections

the elves in the pairs are seperated by a comma
"""

def overlaps(from1, to1, from2, to2):
    if from1 <= from2 <= to1 or from1 <= to2 <= to1:
        return True
    return False

def part2():
    count = 0
    for line in lines:
        elves = line[0].split(",")
        elf1 = elves[0]
        elf2 = elves[1]
        from1 = int(elf1.split("-")[0])
        to1 = int(elf1.split("-")[1])
        from2 = int(elf2.split("-")[0])
        to2 = int(elf2.split("-")[1])
        if overlaps(from1, to1, from2, to2) or overlaps(from2, to2, from1, to1):
            count += 1
    return count

print("Part 2:", part2())