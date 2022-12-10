#https://adventofcode.com/2022/day/5

# Part 1
"""
Credits to studying-asyouwere for helping me!
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
import re, copy # re is needed for regex, copy is needed for deepcopy. both are in the standard library

with open('input.txt', 'r') as file:
    stackUnparsed, instructionData = file.read().split('\n\n')
    stackUnparsed = stackUnparsed.split('\n')
    instructionData = instructionData.split('\n')

stackLast = stackUnparsed.pop() # last line of the stack

# Stack processing

stack = {}
loc = {}
ordering = []
for i in range(len(stackLast)):
    if stackLast[i] != ' ':
        stack[stackLast[i]] = []
        loc[stackLast[i]] = i
        ordering.append(stackLast[i])

for line in reversed(stackUnparsed):
    for key in loc.keys():
        if line[loc[key]] != ' ':
            stack[key].append(line[loc[key]])

stack2 = copy.deepcopy(stack) # for part 2. deepcopy is needed to prevent the same list being used


# Instruction processing
for line in instructionData:
    if 'move' in line:
        instructionValues = re.findall(r'(\d+)', line)
        count = int(instructionValues[0])
        fromStack = instructionValues[1]
        toStack = instructionValues[2]

        for i in range(count):
            lastVal = stack[fromStack].pop()
            stack[toStack].append(lastVal)

        stack2[toStack] += stack2[fromStack][-count:]
        stack2[fromStack] = stack2[fromStack][:-count]

print('The answer for the first part is:')
for i in ordering:
    print(stack[i][-1], end = '')
print()

print('The answer for the second part is:')
for i in ordering:
    print(stack2[i][-1], end = '')