def parse_input():
    with open("7i.txt") as file:
        grid = [[c for c in s] for s in file.read().split('\n')]
    return grid

def in_bounds(x, y, grid):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])

def solve():
    grid = parse_input()
    beams = {grid[0].index("S")}
    split_count = 0
    for line in grid[1:]:
        for x in beams.copy():
            if line[x] == '.':
                line[x] = '|'
            elif line[x] == '^':
                split_count += 1
                beams.add(x - 1)
                beams.add(x + 1)
                beams.remove(x)
    return split_count

print(solve())