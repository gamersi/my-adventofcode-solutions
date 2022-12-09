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
import re, copy

with open('input.txt', 'r') as file:
    stack_txt, instruction_data = file.read().split('\n\n')
    stack_txt = stack_txt.split('\n')
    instruction_data = instruction_data.split('\n')

stack_last = stack_txt.pop()

# Stack processing

stack = {}
loc = {}
ordering = []
for ii in range(len(stack_last)):
    if stack_last[ii] != ' ':
        stack[stack_last[ii]] = []
        loc[stack_last[ii]] = ii
        ordering.append(stack_last[ii])

for line in reversed(stack_txt):
    for key in loc.keys():
        if line[loc[key]] != ' ':
            stack[key].append(line[loc[key]])

stack2 = copy.deepcopy(stack)


# Instruction processing
for line in instruction_data:
    if 'move' in line:
        inst_values = re.findall(r'(\d+)', line)
        count = int(inst_values[0])
        ff = inst_values[1]
        tt = inst_values[2]

        for ii in range(count):
            pop_val = stack[ff].pop()
            stack[tt].append(pop_val)

        stack2[tt] += stack2[ff][-count:]
        stack2[ff] = stack2[ff][:-count]

print('The answer for the first part is:')
for ii in ordering:
    print(stack[ii][-1], end = '')
print()

print('The answer for the second part is:')
for ii in ordering:
    print(stack2[ii][-1], end = '')