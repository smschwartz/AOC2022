import functools
import operator
from collections import deque


def manhattan(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
with open("input18.txt") as f:
    lines = f.readlines()

def getneighbors(n,maxdim):
    x,y,z = n 
    neighbors = [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]
    return [p for p in neighbors if p[0] in range(0,maxdim) and p[1] in range(0,maxdim) and p[2] in range(0,maxdim)]

def printgrid(grid):
    for r in grid:
        print(r)

points = []
for line in lines:
    x,y,z = line.split(',')
    points.append((int(x),int(y),int(z)))

maxdim = max([y for z in [list(x) for x in points] for y in z]) + 2
grid = [[[0 for z in range(0,maxdim)] for y in range(0,maxdim)] for x in range(0,maxdim)]

for p1 in points:
    grid[p1[0]][p1[1]][p1[2]] = 1

distances = [manhattan(p1,p2) for p1 in points for p2 in points]
adjacent = distances.count(1)
surface = len(points)*6-adjacent
print("part a: surface",surface)

q = deque([(0,0,0)])
while q:
    n = q.popleft()
    x,y,z = n 
    if not grid[x][y][z]:  
        grid[x][y][z] = 2    
        q.extend(getneighbors(n,maxdim))

air = deque([])
for i,x in enumerate(grid):
    for j,y in enumerate(x):
        for k,z in enumerate(y):
            if not z:
                air.append((i,j,k))

airsurface = 0
for a in air:
    x,y,z = a
    neighbors = getneighbors(a,maxdim)
    solid = [(x,y,z) for (x,y,z) in neighbors if grid[x][y][z] == 1]
    airsurface += len(solid)

print("part b: outside surface",surface - airsurface)






    

