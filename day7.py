#day 7
#star 13

from collections import defaultdict
import itertools
with open('day7.txt', 'r') as f:
    content = [x.strip() for x in f.readlines()]

steps = []
for line in content:
    words = line.split()
    if len(words)  < 2:
        continue
    pair = (words[1], words[7])
    steps.append(pair)

chart = defaultdict(list)
cp2 = defaultdict(list)
for k, v in steps:
    chart[k].append(v)
    cp2[k].append(v)

items = set()
for key in chart.keys():
    for element in chart[key]:
        if element not in items:
            items.add(element)
start = list(set(chart.keys()) - items)
visited = []
def traverse(nodes):
    if len(nodes) == 0:
        return ''
    current = nodes.pop(0)
    visited.append(current)
    iteration = chart[current]
    chart.pop(current)
    remaining = list(itertools.chain.from_iterable(chart.values()))
    for item in iteration:
        if item not in nodes and item not in visited and item not in remaining:
            nodes.append(item)
            list.sort(nodes)
    return current + traverse(nodes)
print "Part 1: ", traverse(start)

#star 14
import sys
import heapq
from pprint import pprint
from collections import defaultdict

class Worker:
    def __init__(self):
        self.task = None
        self.done = False
        self.working_for = 0

    def set_task(self, task):
        self.task = task
        self.done = False
        self.working_for = (ord(task) - ord('A') + 1) + 60

    def is_busy(self):
        return self.working_for > 0

    def next_timestep(self):
        if self.is_busy:
            self.working_for -= 1
            if self.working_for == 0:
                self.done = True

lines = [line.strip() for line in content if line.strip()]

connections = []
char_to_succ = defaultdict(list)
char_to_pred = defaultdict(list)

for line in lines:
    split = line.split(' ')
    src, dst = split[1].strip(), split[7].strip()
    connections.append((src, dst))

for (src, dst) in connections:
    char_to_succ[src].append(dst)
    char_to_pred[dst].append(src)

workers = [Worker() for _ in range(5)]

order = []
q = []
starters = set(char_to_succ.keys()) - set(char_to_pred.keys())
for starter in starters:
    heapq.heappush(q, starter)

seconds = 0
while len(order) != 26:
    available_workers = [worker for worker in workers if not worker.is_busy()]

    for worker in available_workers:
        if q:
            next_task = heapq.heappop(q)
            worker.set_task(next_task)

    for worker in workers:
        worker.next_timestep()
        if worker.done:
            order.append(worker.task)

            for s in char_to_succ[worker.task]:
                preds = char_to_pred[s]
                if s not in order and all(p in order for p in preds):
                    heapq.heappush(q, s)
            worker.done = False
    seconds += 1
print "Part 2: ", seconds
