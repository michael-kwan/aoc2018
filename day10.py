import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import defaultdict
import re
with open('day10.txt', 'r') as f:
    content = [line.strip() for line in f.readlines()]

stars = [[int(x) for x in re.findall(r'-?\d+', line)] for line in content]
iterations = 0
bunched = False
while not bunched:
    ycoords = defaultdict(int)
    for line in stars:
        ycoords[line[0]] += 1
    if max(ycoords.items(), key=lambda a: a[0])[1] > 7:
        bunched = True
        break
    iterations += 1
    for line in stars:
        line[0] += line[2]
        line[1] += line[3]

print "Part 2:", iterations
xc = []
yc = []
for line in stars:
    xc.append(line[0])
    yc.append(line[1])

plt.scatter(xc,yc)
plt.show()



