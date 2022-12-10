# https://adventofcode.com/2022/day/9

import numpy as np

# file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
moves = [line.split() for line in file.readlines()]

# Part 1
# Credits to medium.com/@datasciencedisciple for helping me with this one

def parseDirection(direction):
    if direction == "U":
        return [1, 0]
    elif direction == "D":
        return [-1, 0]
    elif direction == "R":
        return [0, 1]
    elif direction == "L":
        return [0, -1]


def updateHead(vector, headPos):
    headPos[0] += vector[0]
    headPos[1] += vector[1]
    return headPos


def updateTail(headPos, tailPos, prevHeadPos):
    deltaHead = [headPos[0] - prevHeadPos[0], headPos[1] - prevHeadPos[1]]

    # if the distance between tail and head is greater than 1 in any direction
    if abs(headPos[0] - tailPos[0]) > 1 or \
       abs(headPos[1] - tailPos[1]) > 1:

        # if they were touching before
        if (prevHeadPos[0] == tailPos[0]) or (prevHeadPos[1] == tailPos[1]):
            return [tailPos[0] + deltaHead[0], tailPos[1] + deltaHead[1]]  # move by delta of head

        # if they weren't touching before
        else:
            diff = [headPos[0] - tailPos[0], headPos[1] - tailPos[1]]

            return [tailPos[0] + (np.sign(diff[0]) * min(abs(diff[0]), 1)),
                    tailPos[1] + (np.sign(diff[1]) * min(abs(diff[1]), 1))]

    # if head didn't move away enough
    else:
        return list(tailPos)



def solve(mvLst, numLinks=2):
    curPosLst = [[0, 0] for _ in range(numLinks)]
    linkHist = [(0, 0)]
    for move, i in mvLst:
        for _ in range(int(i)):
            vec = parseDirection(move)
            prevTailPos = tuple(curPosLst[0])
            curPosLst[0] = updateHead(vec, curPosLst[0])
            for tailNum in range(numLinks - 1):
                tailPos = tuple(curPosLst[tailNum + 1])
                curPosLst[tailNum + 1] = \
                    updateTail(
                        curPosLst[tailNum],
                        curPosLst[tailNum + 1],
                        prevTailPos
                    )
                prevTailPos = tailPos
                if tailNum == numLinks - 2:
                    linkHist.append(tuple(curPosLst[numLinks - 1]))
    return len(set(linkHist))

def part1():
    sol = solve(moves, 2)
    return sol

print("Part 1:", part1())

# Part 2

def part2():
    sol = solve(moves, 10)
    return sol

print("Part 2:", part2())