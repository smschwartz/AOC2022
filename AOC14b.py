import functools
import itertools
import json

def printgrid(grid):
	for line in grid:
		print(*line)

def buildgrid(grid,paths,offset):
	for path in paths:
		for i in range(0,len(path)-1):
			match (path[i],path[i+1]):
				case ((y1,x1),(y2,x2)) if x1 == x2:
					for col in range(min(y1,y2),max(y1,y2)+1):
						grid[x1][col-offset] = '#'
				case ((y1,x1),(y2,x2)) if y1 == y2:
					for row in range(min(x1,x2),max(x1,x2)+1):
						grid[row][y1-offset] = '#'

def movesand(grid,loc):
	match loc[0],loc[1]:
		#fell out bottom
		case c,r if r+1>len(grid)-1:
			return False
		case c,r if grid[r+1][c] == '.':
			grid[r+1][c] = 'o'
			grid[r][c] = '.'
			return movesand(grid,(c,r+1))
		#fall into abyss to left
		case c,r if c-1<0:
			return False
		case c,r if grid[r+1][c-1] == '.':
			grid[r+1][c-1] = 'o'
			grid[r][c] = '.'
			return movesand(grid,(c-1,r+1))
		#fall into abyss to right
		case c,r if c+1>len(grid[0])-1:
			return False
		case c,r if grid[r+1][c+1] == '.':
			grid[r+1][c+1] = 'o'
			grid[r][c] = '.'
			return movesand(grid,(c+1,r+1))
		#found resting spot
		case _:
			return True


def dropsand(grid,offset):
	loc = (500-offset,0)
	result = movesand(grid,loc)
	return result


def movesandb(grid,loc):
	match loc[0],loc[1]:
		#nozzle blocked
		case c, r if r==0 and grid[r][c] == 'o':
			return False
		case c, r if grid[r+1][c] == '.':
			grid[r+1][c] = 'o'
			grid[r][c] = '.'
			return movesandb(grid,(c,r+1))
		case c, r if grid[r+1][c-1] == '.':
			grid[r+1][c-1] = 'o'
			grid[r][c] = '.'
			return movesandb(grid,(c-1,r+1))
		case c, r if grid[r+1][c+1] == '.':
			grid[r+1][c+1] = 'o'
			grid[r][c] = '.'
			return movesandb(grid,(c+1,r+1))
		# block nozzle and exit
		case c, r if r == 0 and grid[r][c] != 'o':
			grid[r][c] = 'o'
			return True
		#found resting spot
		case _:
			return True

def dropsandb(grid,offset):
	loc = (500-offset,0)
	result = movesandb(grid,loc)
	return result

with open("input14.txt") as f:
    lines = f.read().split('\n')

mincol = None
maxcol = None
maxrow = None
paths = []

for line in lines:
	steps = []
	chunks = line.split(" -> ")
	for chunk in chunks:
		col,row = list(map(int,chunk.split(',')))
		mincol = col if not mincol else min(mincol,col)
		maxcol = col if not maxcol else max(maxcol,col)
		maxrow = row if not maxrow else max(maxrow,row)
		steps.append((col,row))
	paths.append(steps)

offset = mincol
grid = [['.' for c in range(mincol,maxcol+1)] for r in range(0,maxrow+1)]
buildgrid(grid,paths,offset)
sand = 0
while (dropsand(grid,offset)):
	sand += 1
print("part a",sand)

#part b
#not messing with resizing, just make grid as big as possible
mincol = min(mincol,500-(maxrow+2))
offset = mincol
maxcol = max(maxcol+1,500+(maxrow+2))
colrange = maxcol - mincol + 1
grid = [['.' for c in range(0,colrange+1)] for r in range(0,maxrow+2)]
#add floor
grid.append(['#' for c in range(0,len(grid[0]))])
buildgrid(grid,paths,offset)
sand = 0
while (dropsandb(grid,offset)):
	sand += 1
print("part b",sand)





