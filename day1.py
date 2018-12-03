#day 1
#star 1

with open("day1.txt", 'r') as f:
    content = f.readlines()
changes = [x.strip() for x in content]
part1 = sum(changes)
print(part1)

#star2
counter = 0
reaches = []
step = {}
reached = False
while reached == False:
    for num in changes:
        counter += int(num)
        reaches.append(counter)
        if counter not in step.keys():
            step[counter] = 1
        else:
            reached = True
            part2 = counter
            print(part2)
            break;

