def printTable(tables):
	maxWidth = []
	for table in range(len(tables)):
		for item in range(len(tables[table])):
			if item == 0:
				maxWidth.append(len(tables[table][item]))
			else:
				if len(tables[table][item]) > maxWidth[table]:
					maxWidth[table] = len(tables[table][item])
	lengthOfTable = len(tables[0])
	for rows in range(lengthOfTable):
		for elements in range(len(tables)):
			print(tables[elements][rows].rjust(maxWidth[elements]), end =" ")
		print()

tableData = [["apples", "oranges", "cherries", "banana"],
			["Alice", "Bob", "Carol", "David"],
			["dogs", "cats", "moose", "goose"]]

printTable(tableData)