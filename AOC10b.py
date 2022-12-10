import functools
import operator
with open("input10.txt") as f:
    lines = f.readlines()

cycles = []
regx = 1
for line in lines:
    instr = line.split()
    match instr:
        case ['noop'] : cycles.append(regx)
        case ['addx',n] : 
            cycles += [regx, regx]
            regx += int(n)

vipCycles = [(x+1)*cycles[x] for x in (range(19,len(cycles),40))]

print("part a",functools.reduce(operator.add,vipCycles))
print("part b:")
for row,vals in enumerate([cycles[x:x+40] for x in range(0,len(cycles),40)]):
    screenRow = []
    for pixel,val in enumerate(vals):
        regxVal = cycles[row*40+pixel]
        if pixel in range(regxVal-1,regxVal+2):
            screenRow.append('#')
        else:
            screenRow.append('.')
    print("".join([str(i) for i in screenRow]))





    

