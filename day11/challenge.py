# https://adventofcode.com/2022/day/11

import re # regular expressions
from dataclasses import dataclass # dataclasses
from typing import Callable # typing

file = open("./easier-input.txt", "r")
# file = open("./input.txt", "r")
lines = file.read().splitlines()

# Part 1
"""
The input is a list of monkeys and what they do
Starting items is a list of the worry level of each item the monkey has
Operation is how the worry level of the item changes while the monkey is doing the action
The syntax of operation is: new = old <*|+> <value or old>
Then there is a test, if it is divisible by a number, and then there are two cases:
    Test: divisable by <number>
        If true: throw to monkey <monkey>
        If false: throw to monkey <monkey>

The monkeys are numbered
The syntax of a monkey is:
Monkey <number>:
  Starting items: <list of worry levels> --> for example 50, 75, 64
  Operation: new = old <*|+> <value or old> --> for example new = old + 1 or new = old * old or new = old * 2
  Test: divisible by <number> --> for example divisible by 2
    If true: throw to monkey <number>
    If false: throw to monkey <number>

When a monkey throws an item to another monkey, the item with the new worry level is added to the end of the other monkey's list of items
they do turns and these then group into rounds
At the end the goal is to find the monkey business wich is calculated by multiplying the total times the two monkeys with the highest rate of inspecting items has inspected an item. The rate is the number of items inspected.
The simulation should do 20 rounds and then return the monkey business
"""

def allIntegers(line: str):
    return [int(x) for x in re.findall(r"\d+", line)]

def firstInt(line: str):
    integers = allIntegers(line)
    if(len(integers) == 0): return ValueError("No integers in line")
    return integers[0]

@dataclass
class Monkey:
    monkeyId: int
    currentItems: list[int]
    updateWorryScore: Callable[[int], int]
    getThrowToId: Callable[[int], int]
    allMonkeys: list["Monkey"]

    noInspections: int = 0

    def throwFirstItem(self):
        worryScore = self.currentItems.pop(0)
        newWorryScore = self.updateWorryScore(worryScore)
        newMonkeyId = self.getThrowToId(newWorryScore)
        self.allMonkeys[newMonkeyId].receiveItem(newWorryScore)
        self.noInspections += 1

    def throwAllItems(self):
        while(len(self.currentItems) > 0):
            self.throwFirstItem()

    def receiveItem(self, worryScore: int):
        self.currentItems.append(worryScore)

def parseMonkey(lines: list[str], monkeyId: int, allMonkeys: list[Monkey]):
    linesIterator = iter(lines)
    line = next(linesIterator)
    monkeyId = firstInt(line)

    line = next(linesIterator)
    currentItems = allIntegers(line)

    line = next(linesIterator)
    operationUnparsed = line.replace("  Operation: ", "")
    operation = parseOperation(operationUnparsed)

    def updateWorryScore(worryScore: int):
        return operation(worryScore) // 3

    getThrowToId = parseGetThrowToId(next(linesIterator), next(linesIterator), next(linesIterator))

    monkey = Monkey(monkeyId, currentItems, updateWorryScore, getThrowToId, allMonkeys)
    return monkey

def parseOperation(operationUnparsed: str):
    if(operationUnparsed == "new = old * old"):
        return lambda x: x * x
    elif(operationUnparsed.startswith("new = old + ")):
        return lambda x: x + firstInt(operationUnparsed)
    elif(operationUnparsed.startswith("new = old * ")):
        return lambda x: x * firstInt(operationUnparsed)
    else:
        raise ValueError("Unknown operation")

def parseGetThrowToId(line1: str, line2: str, line3: str):
    if not line1.startswith("  Test: divisible by "): raise ValueError("Unknown test")
    if not line2.startswith("    If true: throw to monkey "): raise ValueError("Unknown if true")
    if not line3.startswith("    If false: throw to monkey "): raise ValueError("Unknown if false")

    divisor = firstInt(line1)
    trueMonkeyId = firstInt(line2)
    falseMonkeyId = firstInt(line3)

    return TestDivisable(divisor, trueMonkeyId, falseMonkeyId)

@dataclass
class TestDivisable:
    divisor: int
    trueMonkeyId: int
    falseMonkeyId: int

    def __call__(self, worryScore: int):
        if worryScore % self.divisor == 0:
            return self.trueMonkeyId
        else:
            return self.falseMonkeyId

def parseLines(lines: list[str]):
    nextMonkeyStart = 0
    monkeys = []
    while(nextMonkeyStart < len(lines)):
        monkeyLines = lines[nextMonkeyStart:nextMonkeyStart + 6] # 6 lines per monkey
        monkey = parseMonkey(monkeyLines, len(monkeys), monkeys)
        monkeys.append(monkey)
        nextMonkeyStart += 7 # 7 lines between monkeys because of the empty line
    return monkeys

def doRound(monkeys: list[Monkey]):
    for monkey in monkeys:
        monkey.throwAllItems()

def part1():
    monkeyBusiness = 0
    monkeys = parseLines(lines)
    for i in range(20):
        doRound(monkeys)

    inspectionCount = [monkey.noInspections for monkey in monkeys]
    inspectionCount.sort(reverse=True)
    monkeyBusiness = inspectionCount[0] * inspectionCount[1]
    return monkeyBusiness

print("Part 1:", part1())

# Part 2
"""
Part 2 description
"""

# def part2():
#     monkeyBusiness = 0
#     monkeys = parseLines(lines)
#     for i in range(10_000):
#         doRound(monkeys)

#     inspectionCount = [monkey.noInspections for monkey in monkeys]
#     inspectionCount.sort(reverse=True)
#     monkeyBusiness = inspectionCount[0] * inspectionCount[1]
#     return monkeyBusiness

# print("Part 2:", part2())