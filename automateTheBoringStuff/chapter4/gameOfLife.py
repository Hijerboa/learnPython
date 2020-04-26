#Conway's game of life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of lists for the cells
nextCells = []
for x in range(WIDTH):
	column = [] #create a new column
	for y in range(HEIGHT):
		if random.randint(0,1) == 0:
			column.append('#') #add a living cell
		else:
			column.append(" ") #add a dead cell
		nextCells.append(column) #nextCells is a list of column lists

while True: #main program loop
	print('\n\n\n\n\n') #Separate each step with newlines
	currentCells = copy.deepcopy(nextCells)
	#Print Current Cells on the screen
	for y in range(HEIGHT):
		for x in range(WIDTH):
			print(currentCells[x][y], end="") #print the # or space
		print() #print a new line at the end of each row

	#Calculate the next step's cells based on the current cells
	for x in range(WIDTH):
		for y in range(HEIGHT):
			#Get neighboring coordinates
			# '%WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
			leftCoord = (x - 1) % WIDTH
			rightCoord = (x + 1) % WIDTH
			aboveCoord = (y - 1) % HEIGHT
			belowCoord = (y + 1) % HEIGHT

			#Count number of living neightbors
			numNeighbors = 0
			if currentCells[leftCoord][aboveCoord] == "#":
				numNeighbors += 1 #Top Left
			if currentCells[x][aboveCoord] == "#":
				numNeighbors += 1 #Top
			if currentCells[rightCoord][aboveCoord] == "#":
				numNeighbors += 1 #Top Right
			if currentCells[leftCoord][y] == "#":
				numNeighbors += 1 #Left
			if currentCells[rightCoord][y] == "#":
				numNeighbors += 1 #Right
			if currentCells[leftCoord][belowCoord] == "#":
				numNeighbors += 1 #Bottom Left
			if currentCells[x][belowCoord] == "#":
				numNeighbors += 1 #Below
			if currentCells[rightCoord][belowCoord] == "#":
				numNeighbors += 1 #Bottom Right

			#Set Current Cell based on game of life rules:
			if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
				#Living cells with 2 or 3 neighbors stay alive:
				nextCells[x][y] = '#'
			elif currentCells[x][y] == "#" and numNeighbors == 3:
				#Dead cells with 3 alive neighbors become alive:
				nextCells[x][y] = "#"
			else:
				#Everything else dies or stays dead:
				nextCells[x][y] = ' '
	time.sleep(1) #Add a 1 second pause
