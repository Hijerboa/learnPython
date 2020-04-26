#using glob

from pathlib import Path
import os

os.chdir("/home/nick/Documents/Repos/learnPython/automateTheBoringStuff/chapter9/")
p = Path.cwd()
print(list(p.glob("*.py")))
