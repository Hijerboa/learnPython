from pathlib import Path


funFile = open("test.txt")
funFileContents = funFile.read()
print(funFileContents)
funFile = open("test.txt", "a")
funFile.write("\nThis is line written from Python")
funFile.close()
funFile = open("test.txt")
funFileContents = funFile.read()
funFile.close()
print(funFileContents)