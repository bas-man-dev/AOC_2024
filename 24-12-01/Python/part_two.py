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

counts = dict()
for i in right:
  counts[i] = counts.get(i, 0) + 1

for i in left:
  if i in counts:
    result += (int(i) * counts[i])

print(f"Final result: {result}")