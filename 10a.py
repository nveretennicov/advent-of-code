from itertools import product
from dataclasses import dataclass

@dataclass
class Machine:
    desired_state : list[bool]
    buttons : list[list[int]]
    requirements : list[int]

def parse_line(s):
    lists = s.split()
    desired_state_s, button_s_list, requirements_s = lists[0], lists[1:-1], lists[-1]

    desired_state = [c == '#' for c in desired_state_s[1:-1]]
    buttons = [[int(c) for c in button_s[1:-1].split(',')] for button_s in button_s_list]
    requirements = [int(c) for c in requirements_s[1:-1].split(',')]

    return Machine(desired_state, buttons, requirements)

def parse_input():
    with open("10i.txt") as file:
        return [parse_line(line) for line in file.read().split('\n')]

def find_min_button_count(machine):
    button_count = len(machine.buttons)
    min_press_count = button_count

    for press_combination in product([False,True], repeat=button_count):
        resultant_state = [False for _ in range(len(machine.desired_state))]
        for i, button in enumerate(machine.buttons):
            if not press_combination[i]:
                continue
            for state_i in button:
                resultant_state[state_i] = not resultant_state[state_i]

        if resultant_state == machine.desired_state:
            press_count = sum(press_combination)
            min_press_count = min(min_press_count, press_count)
    return min_press_count

def solve():
    machines = parse_input()
    return sum(find_min_button_count(m) for m in machines)

print(solve())