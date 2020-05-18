#Abosolute and Relative paths

from pathlib import Path
Path.cwd().is_absolute() #true
onePath = Path("my/relative/path")
print(Path.cwd() / onePath)