def item_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38

def main():
    with open('day_03_input.txt', 'r') as puzzle_input:
        total_priority = 0
        rucksacks = puzzle_input.read().split('\n')
        for rucksack in rucksacks:
            compartment_1, compartment_2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
            shared_item = list(set(compartment_1) & set(compartment_2))[0]
            total_priority += item_priority(shared_item)

        print(total_priority)

if __name__ == '__main__':
    main()