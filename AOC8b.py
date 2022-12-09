import functools
import operator
from itertools import takewhile

def checkVisible(grid,row,col):
    val = grid[row][col]
    blockedup = any([grid[x][col] >= val for x in range(0,row)])
    blockeddown = any([grid[x][col] >= val for x in range(row+1,len(grid))])
    blockedleft = any([grid[row][x] >= val for x in range(0,col)])
    blockedright = any([grid[row][x] >= val for x in range(col+1,len(grid[row]))])
    return not(blockedup and blockeddown and blockedright and blockedleft)

def calcScenic(grid, row, col):
    val = grid[row][col]
    view = [0,0,0,0]
    ranges = [range(row, 0, -1),range(row+1, len(grid)),range(col,0, -1),range(col+1, len(grid[row]))]

    view[0] = len(list(takewhile(lambda x: grid[x-1][col] < val, ranges[0])))
    view[1] = len(list(takewhile(lambda x: grid[x][col] < val, ranges[1] )))
    view[2] = len(list(takewhile(lambda x: grid[row][x-1] < val, ranges[2] )))
    view[3] = len(list(takewhile(lambda x: grid[row][x] < val, ranges[3] )))

    view = list(map(lambda x,r: x if x == len(r) else x + 1,view,ranges))

    return functools.reduce(operator.mul,view)

with open("input8.txt") as f:
    lines = f.read().split('\n')[:-1]
grid = []
for line in lines:
    line = list(map(int,[*line]))
    grid.append(line)

visibility = [[checkVisible(grid,r,c) for c in range(1,len(grid[0])-1)] for r in range(1,len(grid)-1)]
lowTrees = functools.reduce(operator.add,[r.count(True) for r in visibility])
print(lowTrees + (2 * len(grid)) + (2 * len(grid[0])) - 4)
scenic = [[calcScenic(grid,r,c) for c in range(0,len(grid[0]))] for r in range(0,len(grid))]
maxScenic = functools.reduce(max,[max(x) for x in scenic])
print(maxScenic)