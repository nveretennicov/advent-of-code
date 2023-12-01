def convert_digits(s):
    worded_digits = {
        'one' : 'o1e',
        'two' : 't2o',
        'three' : 't3e',
        'four' : 'f4r',
        'five' : 'f5e',
        'six' : 's6x',
        'seven' : 's7n',
        'eight' : 'e8t',
        'nine' : 'n9e',
    }
        
    new_s = s
    for word, digit in worded_digits.items():
        new_s = new_s.replace(word, digit)
    return new_s

with open("puzzle_input.txt") as file:
    input_lines = file.readlines()

total = 0
for line in input_lines:
    formatted_line = convert_digits(line)
    digits = [char for char in formatted_line if char.isdigit()]
    total += int(digits[0] + digits[-1])

print(total)