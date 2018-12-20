with open('day16.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def addr(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] + register[instr[2]]
    return register
def addi(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] + instr[2]
    return register
def mulr(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] * register[instr[2]]
    return register
def muli(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] * instr[2]
    return register
def banr(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] & register[instr[2]]
    return register
def bani(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] & instr[2]
    return register
def borr(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] | register[instr[2]]
    return register
def bori(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]] | instr[2]
    return register
def setr(instr,before):
    register = list(before)
    register[instr[3]] = register[instr[1]]
    return register
def seti(instr,before):
    register = list(before)
    register[instr[3]] = instr[1]
    return register
def gtrr(instr,before):
    register = list(before)
    register[instr[3]] = 1 if register[instr[1]] > register[instr[2]] else 0
    return register
def gtri(instr,before):
    register = list(before)
    register[instr[3]] = 1 if register[instr[1]] > instr[2] else 0
    return register
def gtir(instr,before):
    register = list(before)
    register[instr[3]] = 1 if instr[1] > register[instr[2]] else 0
    return register
def eqir(instr,before):
    register = list(before)
    register[instr[3]] = 1 if instr[1] == register[instr[2]] else 0
    return register
def eqrr(instr,before):
    register = list(before)
    register[instr[3]] = 1 if register[instr[1]] == register[instr[2]] else 0
    return register
def eqri(instr,before):
    register = list(before)
    register[instr[3]] = 1 if register[instr[1]] == instr[2] else 0
    return register
reg = []
winners = []
opcodes = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtrr,gtri,gtir,eqir,eqrr,eqri]
from collections import defaultdict
poss = defaultdict(list)
for i in range(0, len(lines)):
    if "=" in lines[i]:
        break
    if "Before" in lines[i]:
        before = [int(num) for num in lines[i][lines[i].find('[')+1:lines[i].find(']')].split(',')]
    elif "After" in lines[i]:
        p = []
        after = [int(num) for num in lines[i][lines[i].find('[')+1:lines[i].find(']')].split(',')]
        matches = 0
        reg = before
        results = [func(instr,reg) for func in opcodes]
        for i in range(len(results)):
            if results[i] == after:
                matches += 1
                p.append(i)
        if matches >= 3:
            winners.append(instr)
        poss[instr[0]].append(p)
    else:
        instr = [int(num) for num in lines[i].split()]
ans = defaultdict(defaultdict)
for key in poss.keys():
    freq = defaultdict(int)
    r = poss[key]
    for arr in r:
        for e in arr:
            freq[e] += 1
    ans[key]=freq
link = {}
possibles = range(16)
while len(possibles) != 0:
    for key in ans:
        if len(ans[key]) == 1:
            link[key] = ans[key].keys()[0]
            possibles.remove(key)
            for v in link.values():
                for key2 in ans:
                    if v in ans[key2].keys():
                        del ans[key2][v]
link[2] = 2
reg = [0,0,0,0]
for i in range(len(lines)):
    if '=' in lines[i]:
        start = i
instructions = []
for i in range(start+2,len(lines)):
    instr = [int(num) for num in lines[i].split()]
    reg = opcodes[link[instr[0]]](instr,reg)


print 'Part 1:',len(winners)
print 'Part 2:',reg[0]
