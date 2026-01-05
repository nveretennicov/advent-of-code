def parse_turns():
    with open("1i.txt", "r") as file:
        reports = file.read().split('\n')
    return reports
    
def main():
    turns = parse_turns()
    dial = 50
    zero_count = 0
    for turn in turns:
        dir = 1 if turn[0] == 'L' else -1
        turn_count = int(turn[1:])
        dial += dir * turn_count
        dial = dial % 100
        if dial == 0:
            zero_count += 1
    print(zero_count)

main()