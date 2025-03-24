import os
from pathlib import Path


base = Path(__file__).parent.parent.parent / "data"

print(base)
for file in base.rglob("*Zone.Identifier*"):
    # print(file)
    os.remove(file)