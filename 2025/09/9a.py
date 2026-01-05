def parse_input():
    with open("9i.txt") as file:
        positions = []
        for line in file.read().split('\n'):
            x, y = [int(s) for s in line.split(',')]
            positions.append((x, y))
        return positions

def area(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height

def solve():
    positions = parse_input()
    max_area = 0
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            p1, p2 = positions[i], positions[j]
            max_area = max(max_area, area(p1, p2))
    return max_area

print(solve())