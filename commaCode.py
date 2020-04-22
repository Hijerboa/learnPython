def commafier(list):
	string = ""
	if list[0] == None:
		print("Bro I can't commafie an empty list")
	else:
		for x in list:
			string = string + x + " "
	return string

spam = ["Apples", "Bananas", "Tofu", "Cats"]
string = commafier(spam)
print(string)