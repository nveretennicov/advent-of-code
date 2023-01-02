def split(split_list, chunk_size):
    chunks = []
    for i in range(0, len(split_list), chunk_size):
        chunks.append(split_list[i:i + chunk_size])
    return chunks

def get_shared_item_type(rucksacks):
    for item in rucksacks[0]:
        item_in_every_rucksack = True
        for rucksack in rucksacks[1:]:
            if not item in rucksack:
                item_in_every_rucksack = False
                break
        if item_in_every_rucksack:
            return item

def item_priority(item):
    return ord(item) - 96 if item.islower() else ord(item) - 38

def main():
    with open('day_03_input.txt') as puzzle_input:
        total_priority = 0
        rucksacks = puzzle_input.read().split('\n')
        elf_groups = split(rucksacks, 3)
        shared_items = [get_shared_item_type(rucksacks) for rucksacks in elf_groups]

        print(sum([item_priority(c) for c in shared_items]))

if __name__ == '__main__':
    main()