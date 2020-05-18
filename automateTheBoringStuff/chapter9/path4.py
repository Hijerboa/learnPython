#using cwd in python

from pathlib import Path
import os

print(Path.cwd())
os.chdir("..")
print(Path.cwd())