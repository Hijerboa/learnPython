#making a big text file because I'm bored
from pathlib import Path

funFile = open("BigFun.txt", "a")
for i in range(1000):
    funFile.write("This is line written from Python\n")
funFile.close()