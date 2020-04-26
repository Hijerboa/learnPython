#file/folder contents and size

from pathlib import Path
import os
pathThing = "/home/nick/Documents/Repos/learnPython/"
print(os.path.getsize(pathThing))

print(os.listdir(pathThing))