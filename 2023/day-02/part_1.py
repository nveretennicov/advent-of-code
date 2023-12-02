with open("puzzle_input.txt") as file:
    game_records = file.readlines()
    game_records = [record.strip() for record in game_records]

total = 0
for record in game_records:
    game_id, game = record.split(': ')
    game_id = int(game_id.split(' ')[1])
    
    cube_sets = game.split('; ')
    game_possible = True
    for cube_set in cube_sets:
        cubes_drawn = cube_set.split(', ')        
        for draw in cubes_drawn:
            cube_count, cube_colour = draw.split(' ')
            cube_count = int(cube_count)
            if cube_colour == 'red' and cube_count > 12: game_possible = False
            elif cube_colour == 'green' and cube_count > 13: game_possible = False
            elif cube_colour == 'blue' and cube_count > 14: game_possible = False
    if game_possible:
        total += game_id
    
print(total)