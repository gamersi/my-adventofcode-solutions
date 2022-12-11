from challenge import firstInt, allIntegers, Monkey, parseOperation, parseGetThrowToId, doRound

# file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
lines = file.read().splitlines()

ROUNDS = 10_000

def parseMonkey(lines: list[str], allMonkeys: list[Monkey]):
    linesIterator = iter(lines)
    monkeyId = firstInt(next(linesIterator))

    currentItems = allIntegers(next(linesIterator))

    operationUnparsed = next(linesIterator).replace("  Operation: ", "")
    operation = parseOperation(operationUnparsed)
    
    updateWorryScore = operation

    getThrowToId = parseGetThrowToId(next(linesIterator), next(linesIterator), next(linesIterator))

    monkey = Monkey(monkeyId, currentItems, updateWorryScore, getThrowToId, allMonkeys)
    return monkey

def parseLines(lines: list[str]):
    nextMonkeyStart = 0
    monkeys = []
    while nextMonkeyStart < len(lines):
        monkeyLines = lines[nextMonkeyStart:nextMonkeyStart + 6] # 6 lines per monkey
        monkey = parseMonkey(monkeyLines, monkeys)
        monkeys.append(monkey)
        nextMonkeyStart += 7 # 7 lines between monkeys because of the empty line
    return monkeys

def solve(lines: list[str]):
    monkeys = parseLines(lines)

    testModulos = [monkey.getThrowToId.divisor for monkey in monkeys]
    modProd = 1
    for modulo in testModulos:
        modProd *= modulo

    for i in range(ROUNDS):
        doRound(monkeys)
        print(f"Round {i + 1} done", end="\r")

        for monkey in monkeys:
            monkey.currentItems = [worryScore % modProd for worryScore in monkey.currentItems]

    inspectionCount = [monkey.noInspections for monkey in monkeys]
    inspectionCount.sort(reverse=True)
    return inspectionCount[0] * inspectionCount[1]


def main():
    solution = solve(lines)
    print(f"{solution = }")


if __name__ == "__main__":
    main()