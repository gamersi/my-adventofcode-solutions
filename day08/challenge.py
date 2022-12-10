#https://adventofcode.com/2022/day/8

# file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]

# Part 1
"""
the input is a grid of trees
each digit is a tree
the digits are NOT seperated by spaces or commas
0 is the shortest, 9 is the tallest
A tree is only visible if it is taller than at least one other tree surrounding it
so it has to be visible from at least one side
the outermost trees are all visible
The goal is to count the number of visible trees
"""

def part1():
    count = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i][0]) - 1):
            if lines[i][0][j] > lines[i][0][j-1] or \
               lines[i][0][j] > lines[i][0][j+1] or \
               lines[i][0][j] > lines[i-1][0][j] or \
               lines[i][0][j] > lines[i+1][0][j]:
                tallest1 = True
                tallest2 = True
                tallest3 = True
                tallest4 = True

                k = i - 1
                while k >= 0:
                    if lines[i][0][j] <= lines[k][0][j]:
                        tallest1 = False
                    k -= 1
                k = i + 1


                while k < len(lines):
                    if lines[i][0][j] <= lines[k][0][j]:
                        tallest2 = False
                    k += 1



                k = j - 1
                while k >= 0:
                    if lines[i][0][j] <= lines[i][0][k]:
                        tallest3 = False
                    k -= 1


                k = j + 1
                while k < len(lines[i][0]):
                    if lines[i][0][j] <= lines[i][0][k]:
                        tallest4 = False
                    k += 1


                if (tallest1 or tallest2 or tallest3 or tallest4):
                    count += 1
    count += len(lines) * 2 + len(lines[0][0]) * 2 - 4
    return count
print("Part 1:", part1())

def part2():
    highestScore = 0
    totalScore = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i][0])):
            score1 = 0
            score2 = 0
            score3 = 0
            score4 = 0

            ct = 0
            k = i - 1
            while k >= 0:
                ct += 1
                if lines[i][0][j] <= lines[k][0][j]:
                    score1 = ct
                    break
                k -= 1
            if score1 == 0: score1 = ct


            ct = 0
            k = i + 1
            while k < len(lines):
                ct += 1
                if lines[i][0][j] <= lines[k][0][j]:
                    score2 = ct
                    break
                k += 1
            if score2 == 0: score2 = ct


            ct = 0
            k = j - 1
            while k >= 0:
                ct += 1
                if lines[i][0][j] <= lines[i][0][k]:
                    score3 = ct
                    break
                k = k - 1
            if score3 == 0: score3 = ct


            ct = 0
            k = j + 1
            while k < len(lines[i][0]):
                ct += 1
                if lines[i][0][j] <= lines[i][0][k]:
                    score4 = ct
                    break
                k += 1
            if score4 == 0: score4 = ct

            totalScore = score1 * score2 * score3 * score4
            if totalScore > highestScore: highestScore = totalScore
            totalScore = 0

    return highestScore

print("Part 2:", part2())