#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day03/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(lines)
puzzle_file.close()
santa_x_position = 0
santa_y_position = 0
robo_x_position = 0
robo_y_position = 0
parity = 0 
houses = {}
for char in puzzle_input:
    if parity % 2 == 0:
        if char == '^':
            santa_y_position += 1
        elif char == '>':
            santa_x_position += 1
        elif char == 'v':
            santa_y_position -= 1
        else:
            santa_x_position -= 1 
        houses.setdefault(f'{santa_x_position},{santa_y_position}', 1)
    else:
        if char == '^':
            robo_y_position += 1
        elif char == '>':
            robo_x_position += 1
        elif char == 'v':
            robo_y_position -= 1
        else:
            robo_x_position -= 1 
        houses.setdefault(f'{robo_x_position},{robo_y_position}', 1)
    parity += 1

print(len(houses.keys()))

