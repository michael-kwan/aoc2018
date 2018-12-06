#day 6
#star 11
with open('day6.txt', 'r') as f:
	content = [x.strip().split(',') for x in f]

for i in range(len(content)):
	for j in range(len(content[i])):
		content[i][j] = int(content[i][j])

import numpy as np
points = np.asarray(content)
d = content
min_x = min(x[0] for x in d)-(10000/len(d))-1 #for part 2
max_x = max(x[0] for x in d)+(10000/len(d))+1
min_y = min(x[1] for x in d)-(10000/len(d))-1
max_y = max(x[1] for x in d)+(10000/len(d))+1
print min_x, max_x, min_y, max_y
matr = {}
inbound = set()
for x1 in range(min_x, max_x+1):
	for y1 in range(min_y, max_y+1):
		res = d[0]
		mindist = 1000000000
		dsum = 0
		for (x0, y0) in d:
			dist = abs(x0-x1) + abs(y0-y1)
			dsum += dist
			if dist < mindist:
				mindist = dist
				res = (x0, y0)
			elif dist == mindist and res != (x1, y1):
				res = None
			matr[(x1,y1)] = res
		if dsum < 10000:
			inbound.add((x1,y1))

from collections import defaultdict #wait damn this DS is awesome
rev_mapping = defaultdict(int)
for h in matr:
  if not matr[h]:
    continue
  if h[0] in (min_x, max_x) or h[1] in (min_y, max_y):
    rev_mapping[matr[h]] -= (1 << 31)
  rev_mapping[matr[h]] += 1
print "Part 1: ", max(rev_mapping.values())
print "Part 2: ", len(inbound)

# from scipy.spatial import Voronoi, voronoi_plot_2d
# vor = Voronoi(points)
# import matplotlib.pyplot as plt
# voronoi_plot_2d(vor)
# print vor.regions