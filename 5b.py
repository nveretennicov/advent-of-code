def parse_input():
    with open("5i.txt") as file:
        ranges_s = file.read().strip().split('\n\n')[0]
        id_ranges = []
        for range_s in ranges_s.split('\n'):
            start_s, end_s = range_s.split('-')
            id_range = [int(start_s), int(end_s)]
            id_ranges.append(id_range)
    return id_ranges

def refine_id_ranges(id_ranges):
    id_ranges = sorted(id_ranges, key = lambda x : x[0])
    new_id_ranges = []
    for start, end in id_ranges:
        if not new_id_ranges:
            new_id_ranges.append([start, end])
            continue

        if start <= new_id_ranges[-1][1]: 
            new_id_ranges[-1][1] = max(end, new_id_ranges[-1][1])
        else:
            new_id_ranges.append([start, end])
        print(new_id_ranges)
    return new_id_ranges


def calculate_fresh_count(id_ranges):
    fresh_count = 0
    for r_min, r_max in id_ranges:
        fresh_count += (1 + r_max - r_min)
    return fresh_count

def main(): 
    id_ranges = parse_input()
    refined_id_ranges = refine_id_ranges(id_ranges)
    fresh_count = calculate_fresh_count(refined_id_ranges)
    print(fresh_count)

main()