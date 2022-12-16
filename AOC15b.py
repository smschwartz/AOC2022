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

def possible(y,x,pairs):
	possible = True
	for pair in pairs:
		if not possible:
			break
		dist = pair[0].manhattan(pair[1])
		sensor = pair[0]
		if sensor.manhattan(Position(x,y)) <= dist:
			possible = False
	return possible

def checkEdges(pairs,index,maxcoord):
	def checkPoint(x,y):
		return x in range(0,maxcoord+1) and y in range(0,maxcoord+1) and possible(y,x,pairs)

	sensor = pairs[index][0]
	beacon = pairs[index][1]
	dist = sensor.manhattan(beacon)
	# this is hideous and could be made functional but... I think I'm finished here
	x1 = sensor.x 
	y1 = sensor.y - dist - 1
	x2 = sensor.x
	y2 = sensor.y + dist + 1
	x3 = sensor.x - dist - 1
	y3 = sensor.y
	x4 = sensor.x + dist + 1
	y4 = sensor.y
	for i in range(0,dist):
		if checkPoint(x1,y1):
			return Position(x1,y1)
		x1 -= 1
		y1 += 1
		if checkPoint(x2,y2):
			return Position(x2,y2)
		x2 += 1
		y2 += 1
		if checkPoint(x3,y3):
			return Position(x3,y3)
		x3 += 1
		y3 += 1
		if checkPoint(x4,y4):
			return Position(x4,y4)
		x4 -= 1
		y4 += 1
	return None


with open("input15.txt") as f:
    signals = f.read().split('\n')

mincol = None
maxcol = None
minrow = None
maxrow = None
pairs = []

# parse and find dimensions
for signal in signals:
	signal = signal.split()
	sensor = createPos(signal[2],signal[3])
	beacon = createPos(signal[8],signal[9])
	pairs.append((sensor,beacon))

maxrow = 4000000
maxcol = 4000000

print()
print("looking...")


found = False
res = None
for i,pair in enumerate(pairs):
	if found:
		break
	res = checkEdges(pairs,i,maxrow)
	if res:
		found = True
		print("FOUND",res)
		print(res.x*4000000+res.y)






