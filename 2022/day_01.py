def main():    
    with open('day_01_input.txt', 'r') as puzzle_input:
        item_lists = puzzle_input.read().split('\n\n')
        most_calories_carried = 0
        for item_list in item_lists:
            elf_items = [int(item) for item in item_list.split('\n')]
            total_calories = sum(elf_items)
            most_calories_carried = max(most_calories_carried, total_calories)
            
    print(most_calories_carried)

if __name__ == '__main__':
    main()