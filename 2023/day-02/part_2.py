with open("puzzle_input.txt") as file:
    game_records = file.readlines()
    game_records = [record.strip() for record in game_records]

total = 0
for record in game_records:
    game_id, game = record.split(': ')
    game_id = int(game_id.split(' ')[1])
    
    cube_sets = game.split('; ')
    min_red, min_green, min_blue = 0, 0, 0    
    for cube_set in cube_sets:
        cubes_drawn = cube_set.split(', ')        
        for draw in cubes_drawn:
            cube_count, cube_colour = draw.split(' ')
            cube_count = int(cube_count)
            if cube_colour == 'red': min_red = max(min_red, cube_count)
            elif cube_colour == 'green': min_green = max(min_green, cube_count)
            elif cube_colour == 'blue': min_blue = max(min_blue, cube_count)
    cubes_power = min_red * min_blue * min_green
    total += cubes_power
    
print(total)