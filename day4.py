#day 4
#star 7

with open('day4.txt', 'r') as f:
    content = [x.strip() for x in f.readlines()]

content.sort()
guards = {}
minutes = {}
def parse(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    minute = time.split(':')[1]
    return int(minute)

for i in range(len(content)):
    minute = parse(content[i])
    if 'begins' in content[i]:
        guard = int(content[i].split()[3][1:])
        asleep = None
        if guard not in guards.keys():
            guards[guard] = 60*[0]
        if guard not in minutes.keys():
            minutes[guard] = 0
    elif 'falls' in content[i]:
        asleep = minute
    elif 'wakes' in content[i]:
        arr = guards[guard]
        for i in range(asleep,minute):
            arr[i] += 1
            minutes[guard] += 1
        guards[guard] = arr

maxguard = 0
maxtime = 0
for key in minutes.keys():
    if minutes[key] > maxtime:
        maxguard = key
        maxtime = minutes[key]

besttime = 0
mostcommon = 0
for minute in range(len(guards[maxguard])):
    if mostcommon < guards[maxguard][minute]:
        besttime = minute
        mostcommon = guards[maxguard][minute]
print ("Part 1: " + str(maxguard * besttime))

#star 8
maxguard = 0
maxtime = 0
mostcommon = 0
for key in guards.keys():
    for minute in range(len(guards[key])):
        if mostcommon < guards[key][minute]:
            maxtime = minute
            maxguard = key
            mostcommon = guards[key][minute]

print ("Part 2: " + str(maxguard * maxtime))

