def getSet(s):
	ends = list(map(int,s.split('-')))
	return set(range(ends[0],ends[1]+1))

with open("input4.txt") as f:
	lines = [line.strip() for line in f.readlines()]

subsettotal = 0
overlap = 0
for line in lines:
	ranges = list(map(getSet,line.split(',')))
	if ranges[0].issubset(ranges[1]) or ranges[1].issubset(ranges[0]):
		subsettotal += 1
	if ranges[0].intersection(ranges[1]):
		overlap += 1


print(subsettotal)
print(overlap)
	



