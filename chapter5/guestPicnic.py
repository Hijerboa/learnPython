allGuests = {"Alice": {"Apples": 5, "Pretzels": 12},
			"Bob": {"Ham Sandwiches": 3, "Apples": 2},
			"Carol": {"Cups": 3, "Apple Pies": 1}}

def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought


print("Number of things brought:")
print("-Apples: " + str(totalBrought(allGuests, "Apples")))
print("-Cups: " + str(totalBrought(allGuests, "Cups")))
print("-Cakes: " + str(totalBrought(allGuests, "Cakes")))
print("-Ham Sandwiches: " + str(totalBrought(allGuests, "Ham Sandwiches")))
print("-Apple Pies: " + str(totalBrought(allGuests, "Apple Pies")))