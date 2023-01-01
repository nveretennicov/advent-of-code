def main():    
    with open('day_01_input.txt', 'r') as puzzle_input:
        item_lists = puzzle_input.read().split('\n\n')
        all_calory_totals = []
        for item_list in item_lists:
            elf_items = [int(item) for item in item_list.split('\n')]
            total_calories = sum(elf_items)
            all_calory_totals.append(total_calories)
        all_calory_totals.sort()
    
    print(sum(all_calory_totals[-3:]))

if __name__ == '__main__':
    main()