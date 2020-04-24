def printTable(tables):
	maxWidth = []
	for table in range(len(tables)):
		for item in range(len(tables[table])):
			if item == 0:
				maxWidth.append(len(tables[table][item]))
			else:
				if len(tables[table][item]) > maxWidth[table]:
					maxWidth[table] = len(tables[table][item])
	print(maxWidth)

tableData = [["apples", "oranges", "cherries", "banana"],
			["Alice", "Bob", "Carol", "David"],
			["dogs", "cats", "moose", "goose"]]

printTable(tableData)