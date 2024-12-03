from pathlib import Path
import os

def read_input(day: int):
    filepath = Path(f"{os.environ['HOME']}/code/projects/aoc-2024/inputs/day_{day}.txt")

    with filepath.open('r') as f:
        return f.readlines()