import time, sys
numIndent = 1
indentIncreasing = True

try: 
	while True:
		if numIndent == 0:
			indentIncreasing = True
			print(numIndent*" " + "********")
			numIndent = 1
			time.sleep(0.1)
		elif numIndent < 4:
			if indentIncreasing == True:
				print(numIndent*" " + "********")
				numIndent = numIndent + 1
			elif indentIncreasing == False:
				print(numIndent*" " + "********")
				numIndent = numIndent - 1
			time.sleep(0.1)
		elif numIndent == 4:
			indentIncreasing = False
			print(numIndent*" " + "********")
			numIndent = 3
			time.sleep(0.1)

except KeyboardInterrupt:
	sys.exit()