def parse_input():
    with open("5i.txt") as file:
        ranges_s, ids_s = file.read().strip().split('\n\n')
        ids = [int(id_s) for id_s in ids_s.split('\n')]
        id_ranges = []
        for range_s in ranges_s.split('\n'):
            r_min_s, r_max_s = range_s.split('-')
            id_range = range(int(r_min_s), int(r_max_s) + 1)
            id_ranges.append(id_range)
    return ids, id_ranges

def food_id_spoiled(id, id_ranges):
    for id_range in id_ranges:
        if id in id_range:
            return False
    return True

def main():
    ids, id_ranges = parse_input()
    fresh_count = 0
    for id in ids:
        if not food_id_spoiled(id, id_ranges):
            fresh_count += 1
    print(fresh_count)

main()