with open("input.txt") as f:
	lines = f.readlines()

elves = [0]
for line in lines:
	line = line.rstrip('\n')
	if not line:
		elves.append(0)
	else:
		elves[len(elves)-1] += int(line)

elves.sort(reverse=True)
print(sum(elves[0:3]))
