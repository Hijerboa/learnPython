##Simple program to calculate the likelyhood of a string of 6 Heads appearing in a row in a series of 100 coin flips


import random
numberOfStreaks = 0


for experimentNumber in range(10000):
	array = []
	for x in range(0,100):
		if random.randint(0,1) == 0:
			array.append("H")
		else: 
			array.append("T")
	totalInRow = 0
	i = 0
	while i < 100:
		if array[i] == "H":
			if totalInRow != 5:
				totalInRow += 1
			elif totalInRow == 5:
				numberOfStreaks += 1
				break
		elif array[i] == "T":
			totalInRow = 0
		i += 1
print("Chance of Streak: %s%%" % (numberOfStreaks/100))
