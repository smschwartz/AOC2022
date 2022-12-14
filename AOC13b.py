import functools
import itertools
import json

def checkOrder(left, right):
	match left,right:
		case int(left),int(right):
			if isinstance(left,int) and isinstance(right,int):
				return (left > right) - (left < right)
		case list(left),list(right):
			matched = itertools.zip_longest(left,right)
			for pair in matched:
				match pair:
					case (None,x): return -1
					case (x,None): return 1
					case (x,y) if checkOrder(x,y) != 0: return checkOrder(x,y)
			return 0
		case int(left),list(right):
			left = [left]
			return checkOrder(left,right)
		case _:
			right = [right]
			return checkOrder(left,right)

with open("input13.txt") as f:
    listPairs = f.read().split('\n\n')
correct = 0
for i,pair in enumerate(listPairs):
	left,right = list(map(json.loads,pair.split('\n')))
	res = checkOrder(left,right)
	if checkOrder(left,right) == -1:
		correct += i + 1
print("part a",correct)

with open("input13.txt") as f:
    signals = f.read().split('\n')
signals = [json.loads(signal) for signal in signals if signal]
key1 = [[2]]
key2 = [[6]]
signals.append(key1)
signals.append(key2)
signals.sort(key=functools.cmp_to_key(checkOrder))
print("part b",(signals.index(key1) + 1)*(signals.index(key2) + 1))






