import time

def parse_input():
    with open("9i.txt") as file:
        positions = []
        for line in file.read().split('\n'):
            x, y = [int(s) for s in line.split(',')]
            positions.append((x, y))
        return positions

def rect_area(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height

def rect_overlaps_line(lp1, lp2, rp1, rp2):
    lx1, ly1 = lp1
    lx2, ly2 = lp2
    rx1, ry1 = rp1
    rx2, ry2 = rp2

    rx_min, rx_max = min(rx1, rx2), max(rx1, rx2)
    ry_min, ry_max = min(ry1, ry2), max(ry1, ry2)

    if lx1 == lx2: # vertical bounding line
        ly_min, ly_max = min(ly1, ly2), max(ly1, ly2)
        return rx_min < lx1 < rx_max and ly_max > ry_min and ly_min < ry_max
    elif ly1 == ly2:  # horizontal bounding line
        lx_min, lx_max = min(lx1, lx2), max(lx1, lx2)
        return ry_min < ly1 < ry_max and lx_max > rx_min and lx_min < rx_max

def generate_bounding_lines(positions):
    wrapped_positions = positions[::] + [positions[0]]
    bounding_lines = [(wrapped_positions[i], wrapped_positions[i+1]) for i in range(len(wrapped_positions) - 1)]
    return bounding_lines

def valid_rect(rp1, rp2, bounding_lines):
    for lp1, lp2 in bounding_lines:
        if rect_overlaps_line(lp1, lp2, rp1, rp2):
            return False
    return True

def solve():
    positions = parse_input()
    bounding_lines = generate_bounding_lines(positions)
    max_area = 0

    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            p1, p2 = positions[i], positions[j]
            area = rect_area(p1, p2)
            if area > max_area and valid_rect(p1, p2, bounding_lines):
                max_area = area
    
    return max_area

print(solve())