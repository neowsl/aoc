import importlib
from pathlib import Path

if __name__ == "__main__":
    day = input("Enter day: ")
    day = day.zfill(2)
    part = input("Enter part: ")

    module = importlib.import_module(f"days.day{day}")
    f = getattr(module, f"part{part}")
    with open(Path(__file__).parent.parent / "input" / f"day{day}.txt", "r") as file:
        data = file.read()

    print(f(data))
