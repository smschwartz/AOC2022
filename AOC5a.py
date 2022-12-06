import re
import functools
with open("input5.txt") as f:
	stacks,directions = f.read().split('\n\n')

stacklines = stacks.split('\n')
# find out how many stacks are needed
cols = len(stacklines[-1].split())
stacklines = stacklines[0:-1]

# create empty 'stacks'
piles = [[] for _ in range(cols)]
for line in stacklines:
	crates = [line[x].strip() for x in range(1,len(line),4)]
	for i,crate in enumerate(crates):
		if crate:
			piles[i].append(crate)

for p in piles:
	p.reverse()

steps = (directions.split('\n'))[:-1]
for step in steps:
	#get the numbers out of the line
	times,source,dest = list(map(int,re.findall('\d+',step)))
	for i in range(times):
		piles[dest-1].append(piles[source-1].pop())

answer = [x.pop() for x in piles]
print(str(functools.reduce(lambda x,y: x + y, answer)))
