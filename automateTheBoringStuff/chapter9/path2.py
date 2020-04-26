from pathlib import Path
print(Path("spam") / "bacon" / "eggs")
print(Path("spam") / Path("bacon/eggs"))
print(Path("spam") / Path("bacon", "eggs"))
