from dataclasses import dataclass
from z3 import *

@dataclass
class Machine:
    desired_state : list[bool]
    buttons : list[list[int]]
    target : list[int]

def parse_line(s):
    lists = s.split()
    desired_state_s, button_s_list, target_s = lists[0], lists[1:-1], lists[-1]

    desired_state = [c == '#' for c in desired_state_s[1:-1]]
    buttons = [[int(c) for c in button_s[1:-1].split(',')] for button_s in button_s_list]
    target = [int(c) for c in target_s[1:-1].split(',')]

    return Machine(desired_state, buttons, target)

def parse_input():
    with open("10i.txt") as file:
        return [parse_line(line) for line in file.read().split('\n')]

def find_min_button_count(machine):
    x = [Int(f'button_{i}') for i in range(len(machine.buttons))]
    opt = Optimize()
    
    for i in range(len(machine.buttons)):
        opt.add(x[i] >= 0)
    
    for counter_i in range(len(machine.target)):
        effects = []
        for button_i in range(len(machine.buttons)):
            if counter_i in machine.buttons[button_i]:
                effects.append(x[button_i])
        opt.add(Sum(effects) == machine.target[counter_i])
    
    opt.minimize(Sum(x))
    
    if opt.check() == sat:
        model = opt.model()
        solution = [model[x[i]].as_long() for i in range(len(machine.buttons))]
        return sum(solution)

def solve():
    machines = parse_input()
    return sum(find_min_button_count(m) for m in machines)

print(solve())