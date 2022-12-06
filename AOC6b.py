
with open("input6.txt") as f:
	signal = f.read().split('\n')[0]

#for part a, l=4. for part b, l = 14
l = 14
blocks = [signal[x:x+l] for x in range(0,len(signal)-l-1)]
for i,block in enumerate(blocks):
	if (len(set(block)) == l):
		print(i+l)
		break
