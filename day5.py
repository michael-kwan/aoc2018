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
	string = content[0]
	filt = re.compile(letter, re.IGNORECASE)
	string = filt.sub('', string)
	num = collapse(string)
	res[letter] = num

minans = 50000
for key in res.keys():
	if res[key] < minans:
		minans = res[key]

print ("Part 2: " + str(minans))

