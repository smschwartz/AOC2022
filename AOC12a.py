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
    if pos.row < len(graph) - 1 and (graph[pos.row+1][pos.col] in [val,val + 1]):
        moves.append(Position(pos.row+1,pos.col))
    if pos.row > 0 and (graph[pos.row-1][pos.col] in [val,val + 1]):
        moves.append(Position(pos.row-1,pos.col))
    if pos.col > 0 and (graph[pos.row][pos.col-1] in [val,val + 1]):
        moves.append(Position(pos.row,pos.col-1))
    if pos.col < len(graph[0]) - 1 and (graph[pos.row][pos.col+1] in [val,val + 1]):
        moves.append(Position(pos.row,pos.col+1))
    return moves

def remove_redundant(path,moves):
    return [m for m in moves if not(m in path)]

def extendPath(path,moves):
    return list(map(lambda x: path + [x],moves))


def ids(graph,openlist,dlimit):
    goalPath = None
    while not goalPath:
        if not openlist:
            break
        elif openlist[0][-1] == end:
            goalPath = openlist[0]
        elif (len(openlist[0]) - 1) >= dlimit:
            openlist.pop(0)
        else:
            path = openlist.pop(0)
            newpaths = extendPath(path,remove_redundant(path,successors(graph,path[-1])))
            openlist = newpaths + openlist
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

openlist = [[start]]
goalPath = None

dlimit = 1
while not goalPath:
    openlist = [[start]]
    print("ids with depth",dlimit)
    goalPath = ids(graph,openlist,dlimit)
    dlimit += 1


print(goalPath,len(goalPath))







    

