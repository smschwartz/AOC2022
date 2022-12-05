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
	# this is ugly -- go along and grab letter every 4 columns (if it exists)
	i = 1
	for col in range(0,cols):
		crate = line[i:i+1]
		i += 4
		if crate.strip():
			(piles[col]).append(crate)

for p in piles:
	p.reverse()

steps = directions.split('\n')
# get rid of dumb blank line
steps = steps[:-1]
for step in steps:
	# get all of the numbers out of the line
	boxes,source,dest = list(map(int,re.findall('\d+',step)))
	# get the substack to be moved
	pile = piles[source-1][-boxes:]
	# remove those from original stack
	piles[source-1] = piles[source-1][:-boxes]
	# add to new stack
	for b in pile:
		piles[dest-1].append(b)



answer = [x.pop() for x in piles]
print(str(functools.reduce(lambda x,y: x + y, answer)))



