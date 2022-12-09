import functools
import operator
from itertools import takewhile
from dataclasses import dataclass

def checkVisible(grid,row,col):
	val = grid[row][col]
	blockedup = any([grid[x][col] >= val for x in range(0,row)])
	blockeddown = any([grid[x][col] >= val for x in range(row+1,len(grid))])
	blockedleft = any([grid[row][x] >= val for x in range(0,col)])
	blockedright = any([grid[row][x] >= val for x in range(col+1,len(grid[row]))])
	return not(blockedup and blockeddown and blockedright and blockedleft)

def calcScenic(grid, row, col):
	def isShort(r,c):
		return lambda x: grid[r(x)][c(x)] < val

	@dataclass
	class dir:
		count: int
		dirRange: list
		lambdas: tuple

	val = grid[row][col]
	dirs = {
	'Up' : dir(0,range(row, 0, -1),(lambda x: x-1, lambda x: col)),
	'Down' : dir(0,range(row+1, len(grid)),(lambda x: x,lambda x: col)),
	'Left' : dir(0, range(col,0, -1), (lambda x: row, lambda x: x - 1)),
	'Right': dir(0, range(col+1, len(grid[row])), (lambda x: row, lambda x: x))
	}

	for d in dirs.values():
		d.count = len(list(takewhile(isShort(d.lambdas[0],d.lambdas[1]), d.dirRange)))
		
	view = list(map(lambda x,r: x if x == len(r) else x + 1,[d.count for d in dirs.values()],[d.dirRange for d in dirs.values()]))
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


