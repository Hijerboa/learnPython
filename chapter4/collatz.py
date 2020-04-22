import sys

def collatz(number):
	try:
		numInt = int(number)
		if numInt == 1:
			sys.exit()
		elif(numInt % 2) == 0:
			numInt = numInt/2
			print(numInt)
			collatz(numInt)
		else:
			numInt = numInt * 3
			numInt = numInt + 1
			print(numInt)
			collatz(numInt)
	except ValueError:
		print("Bro that's not an integer")


print("Gimmie a number")
val = input()
collatz(val)