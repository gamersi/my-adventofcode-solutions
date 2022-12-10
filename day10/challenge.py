# https://adventofcode.com/2022/day/10


# file = open("./easiest-input.txt", "r")
# file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]

# Part 1

def part1():
    sigStrSum = 0
    cycleValues = [1]
    for line in lines:
        cmd = line[0]
        if cmd == "noop":
            cycleValues.append(cycleValues[-1]) # noop = no operation. Just add the last value to the list
        elif cmd == "addx":
            for i in range(2):
                if i == 0:
                    cycleValues.append(cycleValues[-1]) # addx = add x to the last value. First Cycle: Just add the last value to the list
                else:
                    cycleValues.append(cycleValues[-1] + int(line[1])) # Second Cycle: Add the last value + x

    sigStrSum = sum([i * cycleValues[i - 1] for i in range(20, 240, 40)]) # sum of every  40th value between 20 and 240. so 20, 60, 100, 140, 180, 220

    return cycleValues, sigStrSum

cycleValues, sigStrSum = part1()
print("Part 1:", sigStrSum)

# Part 2

def part2():
    out = ""
    WIDTH = 40
    LIT = "#"
    DARK = "."
    # LIT = "▮" # unicode block
    # DARK = " " # unicode space

    for i, value in enumerate(cycleValues):
        if value in range((i % WIDTH) - 1, (i % WIDTH) + 2):
            out += LIT
        else:
            out += DARK
        
        if (i + 1) % WIDTH == 0:
            out += "\n"
    
    return out

print("Part 2:", "\n"+part2())