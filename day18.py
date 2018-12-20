import sys, itertools, collections
with open('day17.txt') as f:
    board = [line.strip() for line in f.readlines()]

def step(board):
    N = len(board)
    M = len(board[0])
    result = [[None]*M for i in xrange(N)]

    for i in xrange(N):
        for j in xrange(M):
            counts = collections.Counter()
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    if dx == 0 and dy == 0: continue
                    i2 = i+dx
                    j2 = j+dy
                    if 0 <= i2 < N and 0 <= j2 < M:
                        counts[board[i2][j2]]+=1
            if board[i][j] == '.':
                result[i][j] = '|' if counts['|'] >= 3 else '.'
            elif board[i][j] == '|':
                result[i][j] = '#' if counts['#'] >= 3 else '|'
            else:
                result[i][j] = '#' if (counts['#'] >= 1 and counts['|'] >= 1) else '.'
    return result

for i in range(500):
    board = step(board)
    lumber = 0
    forest = 0
    for row in board:
        for elem in row:
            if elem == '|':
                forest += 1
            elif elem == '#':
                lumber += 1
    print i+1, forest*lumber
