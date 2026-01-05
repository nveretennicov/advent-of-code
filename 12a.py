from dataclasses import dataclass

@dataclass
class Tree:
    width : int
    height : int
    present_i_to_count : dict[int, int]

def parse_present(s):
    area = 0
    for row_s in s.split('\n')[1:]:
        for c in row_s:
            if c == '#':
                area += 1
    return area

def parse_trees(s) -> list[Tree]:
    trees = []
    for tree_s in s.split('\n'):
        area_s, present_counts_s = tree_s.split()[0], tree_s.split()[1:]
        width_s, height_s = area_s[:-1].split('x')
        width, height = int(width_s), int(height_s)
        present_i_to_count = {i : int(present_count_s) for i, present_count_s in enumerate(present_counts_s)}
        trees.append(Tree(width, height, present_i_to_count))
    return trees
        
def parse_input():
    with open("12i.txt") as file:
        line_blocks = [lines for lines in file.read().split('\n\n')]
        present_s_list, trees_s = line_blocks[:-1], line_blocks[-1]
        presents = [parse_present(s) for s in present_s_list]
        trees = parse_trees(trees_s)
        return presents, trees

def solve_tree(tree, presents):
    tree_area = tree.height * tree.width
    present_area = sum(presents[i] * count for i, count in tree.present_i_to_count.items())
    present_count = sum(tree.present_i_to_count.values())

    if present_area > tree_area:
        return False
    if (tree.height // 3) * (tree.width // 3) >= present_count:
        return True
    return False

def solve() -> int:
    presents, trees = parse_input()
    return sum(solve_tree(tree, presents) for tree in trees)

print(solve())