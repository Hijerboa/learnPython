birthdays = {'Alice' : "April 1", "Bob" : "Dec 12", "Carol": "Mar 4"}

while True:
	print("Enter a name: (blank to quit)")
	name = input()
	if name == "":
		break

	if name in birthdays:
		print(birthdays[name] + " is the birday of " + name)
	else:
		print("I do not have birthday information for " + name)
		print("What is their birhday?")
		bday = input()
		birthdays[name] = bday
		print("Birthday database updated")