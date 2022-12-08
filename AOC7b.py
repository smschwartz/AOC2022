import re
import functools

def nav(dirs,target):
    if len(target) == 0:
        return dirs
    return nav(dirs[target[0]],target[1:])

def getDir(dircontents,name):
        if name in dircontents.keys():
            return dircontents[name]
        else:
            print("ERROR")

def getDirsDict():
    with open("input7.txt") as f:
        lines = f.read().split('\n')
        dirs = {'/':{}}
        curdir = dirs
        curpath = []
    for line in lines:
        if re.match('\$ cd [/|\w]+',line):
            name = line.split()[2]
            curdir = getDir(curdir,name)
            curpath.append(name)
        elif re.match('dir \w+',line):
            name = line.split()[1]
            curdir[name] = {}
        elif re.match('\d+ \w+[\.]*\w*',line):
            size = int(line.split()[0])
            name = line.split()[1]
            curdir[name] = size
        elif re.match('\$ cd \.\.',line):
            curpath.pop()
            curdir = nav(dirs,curpath)
    return dirs

def sumDir(dir,smalls,alldem):
    sum = 0
    for item in dir.keys():
        if isinstance(dir[item],dict):
            sum += sumDir(dir[item],smalls,alldem)
        else:
            sum += int(dir[item])
    if sum <= 100000:
        smalls.append(sum)
    alldem.append(sum)
    return sum

dirs = getDirsDict()
smalls = []
alldem = []
total = sumDir(dirs, smalls,alldem)
alldem.sort()
print("Total used:",total)
print("Smalls for part a:",functools.reduce(lambda x,y: x + y, smalls))
needed = 30000000 - (70000000 - total)
print("Space Needed for part b:",needed)
for n in alldem:
    if n> needed:
        print("Delete this:",n)
        break



