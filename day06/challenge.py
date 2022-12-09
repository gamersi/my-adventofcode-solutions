#https://adventofcode.com/2022/day/6

#file = open("./easier-input.txt", "r")
file = open("./input.txt", "r")
lines = file.readlines()
lines = [line.split() for line in lines]

# Part 1
"""
The input is a datastream buffer
the start of a packet ist indicated by 4 different digits

the challenge is to find the first start of a packet and then retrieve the number of digits before that packet marker
"""

def find_packet_marker(markerlen, datastream):
    for i in range(markerlen, len(datastream)):
        cmpstr = datastream[i-markerlen:i]
        # print(cmpstr)
        if len(set(cmpstr)) == markerlen:
            return i
    return -1

print("Part 1:", find_packet_marker(4, lines[0][0]))
print("Part 2:", find_packet_marker(14, lines[0][0]))