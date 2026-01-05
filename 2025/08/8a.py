from collections import namedtuple, Counter
import math

Box = namedtuple('Box', ['x', 'y', 'z'])

def sqr_dist(b1, b2):
    return (b1.x - b2.x) ** 2 + (b1.y - b2.y) ** 2 + (b1.z - b2.z) ** 2

def parse_input():
    with open("8i.txt") as file:
        boxes = []
        for line in file.read().split('\n'):
            x, y, z = (int(s) for s in line.split(','))
            boxes.append(Box(x, y, z))
        return boxes

def get_distance_ordered_pairs(boxes, count):
    pairs = []
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            pair = (boxes[i], boxes[j])
            pairs.append(pair)
    return sorted(pairs, key=lambda p : sqr_dist(p[0], p[1]))[:count]

def solve():
    boxes = parse_input()
    parent = {box: box for box in boxes}

    def find(box):
        if parent[box] != box:
            return find(parent[box])
        return parent[box]
    
    def union(b1, b2):
        root1, root2 = find(b1), find(b2)
        parent[root2] = root1

    pairs = get_distance_ordered_pairs(boxes, 1000)
    for b1, b2 in pairs:
        union(b1, b2)

    circuits = Counter(find(box) for box in boxes)
    sorted_sizes = sorted(circuits.values(), reverse=True)
    return math.prod(sorted_sizes[:3])

print(solve())