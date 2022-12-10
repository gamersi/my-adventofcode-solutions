#https://adventofcode.com/2022/day/7
import os

# file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
data = file.read().strip().split("\n")
subdirs = {}
dirSizes = {}

# Part 1
"""
The input is a terminal log.
Each line starting with "$ " is a command.
Each line starting with everything else is the output of the command.
The commands are executed in order.
The commands:
    - "cd" changes the current directory
        - "cd .." goes up one directory
        - "cd <directory>" goes into the directory
        - "cd /" goes into the outermost directory
    - "ls" lists the files in the current directory
        - output lines formatted as "dir <directory>" are directories
        - output lines formatted as "<filesize(int/number)> <file>" are files

The goal is to create a file tree and calculate the total size of the files in each outermost directory.(recursive)
The output should be a list of directories, which sizes are at most 100000.
"""

for line in data:
    if line[0] == '$':
        
        _, cmd, *directory = line.split() # _ is the $ sign. it tells python to ignore it and not store it
        if cmd == 'cd':
            path = directory[0]
            if path == '/':
                curentDir = path
            else:
                curentDir = os.path.normpath(os.path.join(curentDir, path))
            if curentDir not in subdirs:
                subdirs[curentDir] = []
                dirSizes[curentDir] = 0

    else:
        fileSize, fileName = line.split()
        if fileSize != 'dir':
            dirSizes[curentDir] += int(fileSize)
        else:
            subdirs[curentDir].append(os.path.normpath(os.path.join(curentDir, fileName)))

def computeSize(dirname):
    dirsize = dirSizes[dirname]
    for i in subdirs[dirname]:
        if i in subdirs:
            dirsize += computeSize(i)
    return dirsize

solution1 = 0
for i in subdirs:
    dirsize = computeSize(i)
    if dirsize <= 100000:
        solution1 += dirsize

print('The answer to the first questions is: ' + str(solution1))

# Part 2
"""
The goal is to find the smallest directory that we can delete so that spaceRequired is free.
and to print the size of the directory.
"""

totalSpace = 70000000
spaceRequired = 30000000
spaceUsed = computeSize('/')

deleteDir = totalSpace
for i in dirSizes:
    dirSize = computeSize(i)
    if dirSize >= spaceRequired - (totalSpace - spaceUsed) and dirSize <= deleteDir:
        deleteDir = dirSize

print('The answer to the second questions is: ' + str(deleteDir))