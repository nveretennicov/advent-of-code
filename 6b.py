import math

def parse_input():
    with open("6i.txt") as file:
        rows = file.read().split('\n')
        return rows[:-1], rows[-1]

def solve_problem(nums, sign):
    return sum(nums) if sign == '+' else math.prod(nums)

def solve():
    num_rows, sign_row = parse_input()
    total = 0

    nums = []
    for i in range(len(sign_row) - 1, -1, -1):
        num_s = "0"
        for row_i in range(len(num_rows)):
            digit = num_rows[row_i][i]
            if digit != ' ':
                num_s += digit
        
        num = int(num_s)
        if num != 0:
            nums.append(int(num_s))
            

        sign = sign_row[i]
        if sign != ' ':
            total += solve_problem(nums, sign)
            nums = []

    return total
    

print(solve())