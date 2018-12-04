#day 3
#star 5

import re
import numpy as np

vmax = 0
hmax = 0

with open("day3.txt", 'r') as f:
	content =  [list(map(int, re.findall(r'\d+', x))) for x in f.readlines()]

for line in content:
	if len(line) < 4:
		break;
	vrange = line[2]+line[4]
	hrange = line[1]+line[3]
	if vrange > vmax:
		vmax = vrange
	if hrange > hmax:
		hmax = hrange

mat = np.zeros((vmax, hmax))

for line in content:
	if len(line) < 4:
		break;
	v0 = line[2]
	vm = line[4]+line[2]
	h0 = line[1]
	hm = line[3]+line[1]
	for i in range(v0,vm):
		for j in range(h0,hm):
			mat[i][j] = mat[i][j] + 1

part1 = 0
for i in range(len(mat)):
	for j in range(len(mat[0])):
		if mat[i][j] > 1:
			part1 += 1

with open('day3out.txt', 'wb') as f:
    np.savetxt(f, mat, fmt='%d')

print ("Part 1: "+str(part1))

#star 6
for line in content:
	conflict = False
	if len(line) < 4:
		break;
	v0 = line[2]
	vm = line[4]+line[2]
	h0 = line[1]
	hm = line[3]+line[1]
	for i in range(v0,vm):
		for j in range(h0,hm):
			if mat[i][j] > 1:
				conflict = True

	if conflict == False:
		print ("Part 2: " + str(line[0]))
