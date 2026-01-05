def parse_input():
    id_ranges = []
    with open("2i.txt") as file:
        for id_range_s in file.read().split(','):
            id_min_s, id_max_s = id_range_s.split('-')
            id_ranges.append((int(id_min_s), int(id_max_s)))
    return id_ranges

def id_is_invalid(id):  
    id_s = str(id)
    doubled_id_s = id_s * 2
    cropped_doubled_id_s = doubled_id_s[1:-1]
    return id_s in cropped_doubled_id_s

def main():
    id_ranges = parse_input()
    total = 0
    for id_min, id_max in id_ranges:
        for id in range(id_min, id_max + 1):
            if id_is_invalid(id):
                total += id
    print(total)

main()