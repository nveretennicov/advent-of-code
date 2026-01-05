def pad_input():
    lines = []
    with open("4i.txt") as file:
        file_lines = file.readlines()
        empty_line = '.' * (len(file_lines[0]) + 2) 
        lines.append(empty_line)
        for line in file_lines:
            lines.append(f".{line}.")
        lines.append(empty_line)
    return lines

def roll_is_accessible(x, y, grid):
    neighbour_count = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == dx == 0:
                continue
            if grid[y + dy][x + dx] == '@':
                neighbour_count += 1
    return neighbour_count < 4
 
def main():
    grid = pad_input()
    accesible_count = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == '@' and roll_is_accessible(x, y, grid):
                accesible_count += 1
    print(accesible_count)

main()