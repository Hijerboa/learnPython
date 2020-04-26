#Different parts of the filename

from pathlib import Path

p = Path.cwd()
print("Anchor is: " + str(p.anchor))
print("Parent is: " + str(p.parent))
print("Name is: " + str(p.name))
print("Stem is: " + str(p.stem))
print("Suffix is: " + str(p.suffix))

print(p.parents[0])