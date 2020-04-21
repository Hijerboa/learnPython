def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print("Bro you can't just like, put a 0 in there man")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(5235))