from pathlib import Path
p = Path("test.txt")
p.write_text("hello world!")
p.read_text()