from collections import defaultdict

def parse_input():
    with open("7i.txt") as file:
        grid = [[c for c in s] for s in file.read().split('\n')]
    return grid

def in_bounds(x, y, grid):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])

def solve():
    grid = parse_input()
    beams = defaultdict(int) 
    beams[grid[0].index("S")] += 1

    split_count = 0
    for line in grid[1:]:
        for x, value in beams.copy().items():
            if line[x] == '.':
                line[x] = '|'
            elif line[x] == '^':
                split_count += 1
                beams[x - 1] += value
                beams[x + 1] += value
                beams[x] = 0
    return sum(beams.values())

print(solve())