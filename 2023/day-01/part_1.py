with open("puzzle_input.txt") as file:
    input_lines = file.readlines()
    
total = 0
for line in input_lines:
    digits = [char for char in line if char.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)