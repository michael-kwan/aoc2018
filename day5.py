#day 5
#star 9

with open('day5.txt', 'r') as f:
    content = [x.strip() for x in f.readlines()]
string = content[0]
changed = True
while changed:
    stack = []
    changed = False
    for char in string:
        if len(stack) == 0:
            stack.append(char)
        else:
            top = stack.pop()
            if (top.isupper() and char == top.lower()) or (top.islower() and char == top.upper()):
                changed = True
            else:
                stack.append(top)
                stack.append(char)
    string = ''.join(stack)
print("Part 1: " +str(len(string)))

#star 10
from string import ascii_lowercase
import re
import time
tstart = time.clock()
def collapse(string):
    changed = True
    while changed:
        stack = []
        changed = False
        for char in string:
            if len(stack) == 0:
                stack.append(char)
            else:
                top = stack.pop()
                if (top.isupper() and char == top.lower()) or (top.islower() and char == top.upper()):
                    changed = True
                else:
                    stack.append(top)
                    stack.append(char)
        string = ''.join(stack)
    return len(string)

res = {}
for letter in ascii_lowercase:
    t0 = time.clock()
    string = content[0]
    filt = re.compile(letter, re.IGNORECASE)
    string = filt.sub('', string)
    num = collapse(string)
    res[letter] = num
    t1 = time.clock()
    print (letter + " in " + str(t1-t0) + " seconds")

minans = 50000
for key in res.keys():
    if res[key] < minans:
        minans = res[key]

print ("Part 2: " + str(minans))
tend = time.clock()
print ("Part 2 in " + str(tend - tstart) + " seconds")

