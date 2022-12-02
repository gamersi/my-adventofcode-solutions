#https://adventofcode.com/2022/day/1

file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]
cals = []
current = 0
largestCal = 0
topThreeTotal = 0

for line in lines:
    if line.__len__() == 0:
        cals.append(current)
        current = 0
    else:
        current += int(line[0])

largestCal = max(cals)

topThreeTotal = sum(sorted(cals, reverse=True)[:3])

print(largestCal, '\n', topThreeTotal)

file.close()