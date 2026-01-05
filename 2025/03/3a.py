def parse_input():
    banks = []
    with open("3i.txt") as file:
        for bank_s in file.read().split('\n'):
            banks.append([int(c) for c in bank_s])
    return banks

def find_max_joltage(bank):
    current_max = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            joltage = bank[i] * 10 + bank[j]
            current_max = max(current_max, joltage)
    return current_max

def main():
    banks = parse_input()
    total = 0
    for bank in banks:
        total += find_max_joltage(bank)
    print(total)

main()