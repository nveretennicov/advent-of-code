import math

def parse_input():
    with open("6i.txt") as file:
        rows = file.read().split('\n')
        num_rows = [[int(s) for s in r.split()] for r in rows[:-1]]
        sign_row = [c for c in rows[-1].split()]
        return zip((row for row in zip(*num_rows)), sign_row)

def solve_problem(nums, sign):
    return sum(nums) if sign == '+' else math.prod(nums)

def solve():
    total = sum(solve_problem(nums, sign) for nums, sign in parse_input())
    print(total)

solve()