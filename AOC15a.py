import functools
import itertools
import json
from dataclasses import dataclass

@dataclass
class Position:
	x: int
	y: int

	def manhattan(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)
	def shift(self,xoffset,yoffset):
		self.x += xoffset
		self.y += yoffset
		return self

def createPos(xstr,ystr):
	xstr = xstr.lstrip("x=")
	xstr = xstr.rstrip(",")
	ystr = ystr.lstrip("y=")
	ystr = ystr.rstrip(":")
	return Position(int(xstr),int(ystr))

def printgrid(grid):
	for line in grid:
		print(*line)

def blockstuff(grid,pair,rowofinterest):
	sensor = pair[0]
	beacon = pair[1]
	dist = sensor.manhattan(beacon)
	if rowofinterest in range(sensor.y-dist,sensor.y+dist+1):
		for x in range(sensor.x-dist,sensor.x+dist+1):
				if sensor.manhattan(Position(x,rowofinterest)) <= dist:
						grid[x] = '#'

def graphpair(grid,pair,rowofinterest):
	sensor = pair[0]
	beacon = pair[1]
	if sensor.y == rowofinterest:
		grid[sensor.x] = 'S'
	if beacon.y == rowofinterest:
		grid[beacon.x] = 'B'

with open("input15.txt") as f:
    signals = f.read().split('\n')

mincol = None
maxcol = None
minrow = None
maxrow = None
pairs = []

# parse and find dimensions. The horror.
for signal in signals:
	signal = signal.split()
	sensor = createPos(signal[2],signal[3])
	beacon = createPos(signal[8],signal[9])
	pairs.append((sensor,beacon))
	dist = sensor.manhattan(beacon)
	minrow = min(beacon.y,sensor.y-dist) if minrow == None else min(minrow,sensor.y-dist,beacon.y)
	maxrow = max(beacon.y,sensor.y+dist) if maxrow == None else max(maxrow,sensor.y+dist,beacon.y)
	mincol = min(beacon.x,sensor.x-dist) if mincol == None else min(mincol,sensor.x-dist,beacon.x)
	maxcol = max(beacon.x,sensor.x+dist) if maxcol == None else max(maxcol,sensor.x+dist,beacon.x)

xoffset = -mincol
yoffset = -minrow
for i,(sensor,beacon) in enumerate(pairs):
	pairs[i] = (sensor.shift(xoffset,yoffset),beacon.shift(xoffset,yoffset))
rowofinterest = 2000000 + yoffset
grid = list(['.' for c in range(mincol,maxcol+1)])

# Yep, leaving this here. Omg.
for pair in pairs:
	blockstuff(grid,pair,rowofinterest)
for pair in pairs:
	graphpair(grid,pair,rowofinterest)

# Yeah, I'm not even rewriting this. I've had it.
count = 0
print("counting...")
for c in grid:
	if (c == '#'):
		count += 1
print(count)




