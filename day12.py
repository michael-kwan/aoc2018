lines = open('day12.txt').read().split('\n')

string = lines[0].split(': ')[1].strip()

rules = {}
for line in lines[2:]:
    if line:
        rule = line.split(' => ')[0]
        result = line.split(' => ')[1]
        rules[rule] = result

def find_sum(string, zero_index):
    sum = 0
    for i in range(len(string)):
        if string[i] == '#':
            sum += i - zero_index

    return sum
diff = 0
zero_index = 0
for iteration in range(500):
    string = '....' + string + '....'
    zero_index += 2
    newstring = ''
    for i in range(2, len(string)-2):
        newstring += rules[string[i-2:i+3]]
    string = newstring
    if iteration % 1 == 0:
        temp = find_sum(string,zero_index)
        diff = temp - diff
        print iteration, temp, diff
        diff = temp




