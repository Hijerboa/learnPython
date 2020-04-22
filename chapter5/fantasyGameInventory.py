#inventory tracker
stuff = {"rope": 1, "torch": 6, "gold coins": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
	print("Inventory: ")
	item_total = 0
	for k, v in inventory.items():
		quantity = v
		itemName = k
		print(str(quantity) + " " + itemName)
		item_total += quantity
	print("Total number of items: " + str(item_total))
	

displayInventory(stuff)	