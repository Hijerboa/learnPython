#total size of all files in a particular folder
from pathlib import Path
import os

totalSize = 0
for filename in os.listdir("/home/nick/Documents/Repos/learnPython/automateTheBoringStuff/chapter9"):
    totalSize = totalSize + os.path.getsize(os.path.join("/home/nick/Documents/Repos/learnPython/automateTheBoringStuff/chapter9", filename))
print(totalSize)
