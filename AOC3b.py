def getPriority(c):
	if c.isupper():
		return ord(c) - ord('A') + 27
	else:		
		return ord(c) - ord('a') + 1

with open("input3.txt") as f:
	lines = [line.strip() for line in f.readlines()]

total = 0
group = []
badgeTotal = 0
for line in lines:
	s1 = set(line[:(len(line)//2)])
	s2 = set(line[len(line)//2:])
	total += getPriority(s1.intersection(s2).pop())
	if (len(group) + 1) % 3:
		group.append(set(line))
	else:
		badge = getPriority((set(line).intersection(group[0],group[1])).pop())
		badgeTotal += badge
		group = []

print("items:",total)
print("badges:",badgeTotal)



