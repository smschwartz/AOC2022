import functools
import operator
from dataclasses import dataclass
import string

@dataclass
class Position:
    row: int
    col: int

def successors(graph,pos):
    moves = []
    val = graph[pos.row][pos.col]
    if pos.row < len(graph) - 1 and (graph[pos.row+1][pos.col] in range(0,val+2)):
        moves.append(Position(pos.row+1,pos.col))
    if pos.row > 0 and (graph[pos.row-1][pos.col] in range(0,val+2)):
        moves.append(Position(pos.row-1,pos.col))
    if pos.col > 0 and (graph[pos.row][pos.col-1] in range(0,val+2)):
        moves.append(Position(pos.row,pos.col-1))
    if pos.col < len(graph[0]) - 1 and (graph[pos.row][pos.col+1] in range(0,val+2)):
        moves.append(Position(pos.row,pos.col+1))
    return moves

def remove_redundant(path,moves):
    return [m for m in moves if not(m in path)]

def extendPath(path,moves):
    return list(map(lambda x: path + [x],moves))

def bfs(graph,openlist,end,limit):
    goalPath = None
    maxpath = len(graph)*len(graph[0])
    bests = [[maxpath for x in range(0,len(graph[0]))] for y in range(0,len(graph))]

    while not goalPath:
        if not openlist:
            break
        elif openlist[0][-1] == end:
            print("FOUND IT!")
            goalPath = openlist[0]
        else:
            path = openlist.pop(0) 
            if len(path) - 1 < limit and (len(path) - 1) < bests[path[-1].row][path[-1].col]:
                bests[path[-1].row][path[-1].col] = len(path) - 1
                newpaths = extendPath(path,remove_redundant(path,successors(graph,path[-1])))
                openlist = openlist + newpaths
    return goalPath

with open("input12.txt") as f:
    graphInput = f.readlines()

origGraph = []
graph = []

start = None
end = None

for row,line in enumerate(graphInput):
    letters = [*line.rstrip()]
    if "S" in letters:
        start = Position(row,letters.index("S"))
    if "E" in letters:
        end = Position(row,letters.index("E"))
    origGraph.append(letters)

for row in origGraph:
    graph.append(list(map(ord,row)))

graph[start.row][start.col] = ord("a")
graph[end.row][end.col] = ord("z")

minLen = len(graph)*len(graph[0])
openlist = [[start]]
goalPath = bfs(graph,openlist,end,minLen)


print("part a",len(goalPath)-1)

pathLens = []

for x in range(0,len(graph)):
    for y in range(0,len(graph[0])):
        if graph[x][y] == ord('a'):
            openlist = [[Position(x,y)]]
            path = bfs(graph,openlist,end,minLen)
            if path:
                minLen = min(minLen,len(path)-1)
                pathLens.append(len(path)-1)
print(pathLens)
print("part b", minLen)








    

