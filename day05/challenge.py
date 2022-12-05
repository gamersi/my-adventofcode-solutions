#https://adventofcode.com/2022/day/5

file = open("./input.txt", "r")
data = file.read()
lines = [line for line in data.split('\n')]

# Part 1
"""
there are 9 stacks of crates in the ship on the giant cargo crane
each crate has a assigned letter
they are in the first few lines of the input file before the empty line and the instructions
the instructions are in the last lines of the input file 
the instructions are structured as follows

move <amount> from <stack> to <stack>

the amount is the amount of crates to move(from the top of the stack)
the stacks are the numbers of the stacks
the instructions are in the order they should be executed
in the end, there should be a string of the letters on the top of each stack in the order of the stacks

example:
input:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

processing outputs:
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

output:
CMP
"""

"""
Context in the current example:
out = [
'[V]     [B]                     [F]',
'[N] [Q] [W]                 [R] [B]',
'[F] [D] [S]     [B]         [L] [P]', 
'[S] [J] [C]     [F] [C]     [D] [G]', 
'[M] [M] [H] [L] [P] [N]     [P] [V]', 
'[P] [L] [D] [C] [T] [Q] [R] [S] [J]', 
'[H] [R] [Q] [S] [V] [R] [V] [Z] [S]', 
'[J] [S] [N] [R] [M] [T] [G] [C] [D]', 
' 1   2   3   4   5   6   7   8   9 ']

out2 = {
    1: ['V', 'N', 'F', 'S', 'M', 'P', 'H', 'J'],
    2: ['Q', 'D', 'J', 'M', 'L', 'R', 'S'],
    3: ['B', 'W', 'S', 'C', 'H', 'D', 'Q', 'N'],
    4: ['L', 'C', 'S', 'R'],
    5: ['B', 'F', 'P', 'T', 'V', 'M'],
    6: ['C', 'N', 'Q', 'R', 'T'],
    7: ['R', 'V', 'G'],
    8: ['R', 'L', 'D', 'P', 'S', 'Z', 'C'],
    9: ['F', 'B', 'P', 'G', 'V', 'J', 'S', 'D']
}"""


def part1():
    rawStacks = []
    switchingPoint = False
    instructions = []
    for line in lines:
        if line == '':
            switchingPoint = True
            continue
        if(switchingPoint):
            instructions.append(line)
        else:
            rawStacks.append(line)

    formattedStacks = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }
    print(len(rawStacks))
    for i in range(len(rawStacks) - 1):
        index: int = 0
        j = 0
        while j <= len(rawStacks[i]) - 1:
            # print(index, rawStacks[i][j])
            if rawStacks[i][j] == '[':
                print(index, rawStacks[i][j+1])
                formattedStacks[index].append(rawStacks[i][j+1])
                index += 1
            elif rawStacks[i][j] == ' ' and rawStacks[i][j+1] == ' ' and rawStacks[i][j+2] == ' ' and rawStacks[i][j+3] == ' ' and rawStacks[i][j+4] == ' ':
                print("skipped")
                j = j+4
                index += 1
            else:
                j+=1
                continue
            j+=1
    return formattedStacks

print("Part 1:", part1())