def parse_input():
    banks = []
    with open("3i.txt") as file:
        for bank_s in file.read().split('\n'):
            banks.append([int(c) for c in bank_s])
    return banks

def find_max_joltage(bank, battery_on_count):
    digits_s = ""
    i = 0
    while battery_on_count > 0:
        max_digit_i = i
        for j in range(i, len(bank) - battery_on_count + 1):
            digit = bank[j]
            if digit > bank[max_digit_i]:
                max_digit_i = j
        
        max_digit = bank[max_digit_i]
        digits_s += str(max_digit)
        i = max_digit_i + 1
        battery_on_count -= 1
    
    return int(digits_s)

def main():
    banks = parse_input()
    total = 0
    for bank in banks:
        total += find_max_joltage(bank, 12)
    print(total)

main()