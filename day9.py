from itertools import cycle
import time
players = 477
hiscore = 7085100

marbles = [0,1]
index = 1
current = 2
scores = {}
players = cycle([i for i in range(1,players+1)])
players.next()
t0 = time.clock()
while current < hiscore:
    turn = players.next()
    if len(marbles) == 0:
        marbles.insert(0, current)
        current += 1
        index = 0
        continue;
    elif current % 23 == 0:
        temp = (index-7)%len(marbles)
        if turn not in scores.keys():
            scores[turn] = current
        else:
            scores[turn] += current
        removed = marbles.pop(temp)
        scores[turn] += removed
        index = temp
        current += 1
    else:
        temp = (index+2)%len(marbles)
        marbles.insert(temp,current)
        index = temp
        current += 1
    if current % 100000 == 0:
        t1 = time.clock()
        print current, t1-t0
        t0 = time.clock()

maxkey = 0
maxvalue = 0
for key in scores.keys():
    if scores[key] > maxvalue:
        maxvalue = scores[key]
        maxkey = key

print maxkey, maxvalue



