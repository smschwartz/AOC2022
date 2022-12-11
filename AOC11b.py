import functools
import operator
class monkey:
    def __init__(self, input):
        lines = input.split('\n')
        self.id = lines[0].split()[1]
        items = lines[1].split()[2:]
        self.items = []
        for item in items:
            item = item.rstrip(',')
            self.items.append(int(item))
        self.op = lines[2].split()[4]
        self.val = lines[2].split()[5]
        self.modby = int(lines[3].split()[3])
        self.inspected = 0
        self.trueTarget = None
        self.falseTarget = None

    def throw(self, item):
        return item % self.modby == 0

    def catch(self, item):
        self.items.append(item)

    def setTargets(self,trueTarget, falseTarget):
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget

    def takeTurn(self,mod):
        for item in self.items:
            self.inspected += 1
            match self.val:
                case "old" : val = item
                case _ : val = int(self.val)

            match self.op:
                case "*": item = item * val
                case "+": item = item + val
            # part a
            # item = item // 3
            item = item % mod
            if (self.throw(item)):
                self.trueTarget.catch(item)
            else:
                self.falseTarget.catch(item)
        self.items = []

    def toString(self):
        retstr =  "This monkey has " + str(self.items) + "\n  and " + self.op + " " + self.val 
        retstr += "\n  and mod by " + str(self.modby)
        retstr += "\n  and throws to " + self.trueTarget.id + " " + self.falseTarget.id
        retstr += "\n  and inspected " + str(self.inspected) + " items\n"
        return retstr

with open("input11.txt") as f:
    monkeyInput = f.read().split('\n\n')

monkeys = []
for block in monkeyInput:
    monkeys.append(monkey(block))

# add targets of throws to monkeys
for i,block in enumerate(monkeyInput):
    lines = block.split('\n')
    t1 = lines[4].split()
    t2 = lines[5].split()
    monkeys[i].setTargets(monkeys[int(t1[5])], monkeys[int(t2[5])])

# compute divisor for part b
mods = [m.modby for m in monkeys]
mod = functools.reduce(operator.mul,mods)
for r in range(0,10000):
    for m in monkeys:
        m.takeTurn(mod)

for m in monkeys:
    print(m.toString())


inspections = [m.inspected for m in monkeys]
inspections.sort()
print(inspections)
print(inspections[-1]*inspections[-2])



    

