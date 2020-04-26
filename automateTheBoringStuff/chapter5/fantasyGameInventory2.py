def displayInventory(inventory):
	print("Inventory: ")
	item_total = 0
	for k, v in inventory.items():
		quantity = v
		itemName = k
		print(str(quantity) + " " + itemName)
		item_total += quantity
	print("Total number of items: " + str(item_total))



def addToInventory(inventory, addedItems):
	for items in dragonLoot:
		if inventory.get(items, 0) == 0:
			inventory[items] = 1
		else:
			inventory[items] = inventory[items] + 1
	return inventory

inv = {"Gold Coin": 42, "Rope": 1}
dragonLoot = ["Gold Coin", "Dagger", "Gold Coin", "Gold Coin", "Ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)