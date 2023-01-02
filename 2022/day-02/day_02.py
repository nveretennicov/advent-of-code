scoring = {
    # Draw scenarios
    ('X', 'A'): 3,
    ('Y', 'B'): 3,
    ('Z', 'C'): 3,
    # Win scenarios
    ('X', 'C'): 6,
    ('Y', 'A'): 6,
    ('Z', 'B'): 6,
}

def calculate_score(opponent_pick, your_pick):
    shape_points = {'X': 1, 'Y': 2, 'Z': 3}
    score = shape_points[your_pick] + scoring.get((your_pick, opponent_pick), 0)
    return score

def main():
    with open('day_02_input.txt', 'r') as puzzle_input:
        rounds = puzzle_input.read().split('\n')
        total_score = 0
        for round in rounds:
            your_pick, opponent_pick = round.split(' ')
            total_score += calculate_score(your_pick, opponent_pick)

        print(total_score)

if __name__ == '__main__':
    main()