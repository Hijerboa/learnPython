#showing how "/" always is used to join paths when using Path
from pathlib import Path
homeFolder = Path("/home/nick/")
subFolder = Path("Oofie")
print((homeFolder / subFolder))
print(str((homeFolder / subFolder)))