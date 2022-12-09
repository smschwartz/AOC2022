from dataclasses import dataclass
from enum import Enum

class Move(Enum):
    U = 1
    D = 2
    L = 3
    R = 4

@dataclass
class Point:
    x : int
    y : int
    def move(self, d : Move):
        match d:
            case Move.U: self.y += 1
            case Move.D: self.y -= 1
            case Move.L: self.x -= 1
            case Move.R: self.x += 1
    def vals(self):
        return (self.x,self.y)

def adjustTail(head: Point, tail: Point):
    if head == tail:
        return
    match [head, tail]:
        case [h,t] if h.x - t.x == 2:
            tail.move(Move.R)
            if h.y > t.y:
                tail.move(Move.U)
            else:
                tail.move(Move.D)
        case [h,t] if t.x - h.x == 2:
            tail.move(Move.L)
            if h.y > t.y:
                tail.move(Move.U)
            else:
                tail.move(Move.D)  
        case [h,t] if h.y - t.y == 2:
            tail.move(Move.U)
            if h.x > t.x:
                tail.move(Move.R)
            else:
                tail.move(Move.L)
        case [h,t] if t.y - h.y == 2:
            tail.move(Move.D)
            if h.x > t.x:
                tail.move(Move.R)
            else:
                tail.move(Move.L)

with open("input9.txt") as f:
    lines = f.readlines()

# for part a, just use this for current
#current = [Point(0,0),Point(0,0)]
current = [Point(0,0) for x in range(0,10)]
spots = {(0,0)}
for line in lines:
    dir,count = line.split()
    for i in range(0,int(count)):
        current[0].move(Move[dir])
        for i,knot in enumerate(current[:-1]):
            adjustTail(current[i],current[i+1])
        spots.add(current[len(current)-1].vals())
print(len(spots))


    

