with open("input2.txt") as f:
	lines = f.readlines()

myChoice = {
	'Rock' : 0,
	'Paper' : 0,
	'Scissors' : 0
}
Outcomes = {
	'Win' : 0,
	'Draw' : 0,
	'Loss' : 0
}

for line in lines:
	plays = line.split()
	match plays[1]:
		case 'X' : Outcomes['Loss'] += 1
		case 'Y' : Outcomes['Draw'] += 1
		case 'Z' : Outcomes['Win'] += 1
	match (plays[0],plays[1]):
		case ('A','X') | ('B','Z') | ('C','Y'): myChoice['Scissors'] += 1
		case ('A','Y') | ('B','X') | ('C','Z'): myChoice['Rock'] += 1
		case ('A','Z') | ('B','Y') | ('C','X'): myChoice['Paper'] += 1

choiceScore = myChoice['Rock'] + myChoice['Paper'] * 2 + myChoice['Scissors'] * 3
outcomeScore = Outcomes['Win'] * 6 + Outcomes['Draw'] * 3 
print(choiceScore + outcomeScore)