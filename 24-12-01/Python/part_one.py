#!/usr/bin/python
left = []
right =[]
result = 0

with open('../input.txt', 'r') as file:

    for line in file:
        line = line.split()

        left.append(line[0])
        right.append(line[1])
left = sorted(left)
right = sorted(right)

for difference in range(len(left)):
    absolute = (int(left[difference]) - int(right[difference]))
    result += (abs(absolute))
print(f"Final difference: {result}")