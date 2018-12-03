#day 2
#star 3

with open("day2.txt", 'r') as f:
    content = [x.strip() for x in f.readlines()]

count = []
for name in content:
    letters = {}
    app = 2*[0]
    for letter in name:
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1
    for key in letters.keys():
        if letters[key] == 2:
            app[0] = 1
        elif letters[key] == 3:
            app[1] = 1
    count.append(app)

part1 = [sum(x) for x in zip(*count)]
print("Part 1: " + str(part1[0]*part1[1]))

#star4

for i in content:
    for j in content:
        differences = 0
        for pos, char in enumerate(i):
            if j[pos] != char:
                differences += 1
        if differences == 1:
            part2 = [char for pos, char in enumerate(i) if j[pos] == char]
            print ("Part 2: " + ''.join(part2))


