#https://adventofcode.com/2022/day/2

file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]
currentScore = 0
totalScore = 0

"""
opponent:
A - Rock
B - Paper
C - Scissors

You:
X - Rock
Y - Paper
Z - Scissors

Score:
A beats Z
B beats X
C beats Y

1 for Rock
2 for Paper
3 for Scissors

+ 
0 for lose
3 for draw
6 for win
"""

for line in lines:
    a = line[0]
    b = line[1]
    if b == "X": currentScore += 1
    elif b == "Y": currentScore += 2
    elif b == "Z": currentScore += 3

    if a == "A":
        if b == "Z":
            currentScore += 0
        elif b == "X":
            currentScore += 3
        elif b == "Y":
            currentScore += 6
    elif a == "B":
        if b == "Z":
            currentScore += 6
        elif b == "X":
            currentScore += 0
        elif b == "Y":
            currentScore += 3
    elif a == "C":
        if b == "Z":
            currentScore += 3
        elif b == "X":
            currentScore += 6
        elif b == "Y":
            currentScore += 0
    
    totalScore += currentScore
    currentScore = 0

print('Part1: ', totalScore)

# Part 2
"""
opponent:
A - Rock
B - Paper
C - Scissors

You:
X - Lose
Y - Draw
Z - Win

Score:
1 for Rock
2 for Paper
3 for Scissors

+ 
0 for lose
3 for draw
6 for win
"""

totalScore2 = 0
currentScore2 = 0

for line in lines:
    a = line[0]
    b = line[1]

    if b == "X":
        if a == "A":
            currentScore2 += 3
        elif a == "B":
            currentScore2 += 1
        elif a == "C":
            currentScore2 += 2
    elif b == "Y":
        if a == "A":
            currentScore2 += 1
        elif a == "B":
            currentScore2 += 2
        elif a == "C":
            currentScore2 += 3
    elif b == "Z":
        if a == "A":
            currentScore2 += 2
        elif a == "B":
            currentScore2 += 3
        elif a == "C":
            currentScore2 += 1


    if b == "X": currentScore2 += 0
    elif b == "Y": currentScore2 += 3
    elif b == "Z": currentScore2 += 6
    
    
    totalScore2 += currentScore2
    currentScore2 = 0

print('Part2: ', totalScore2)

file.close()