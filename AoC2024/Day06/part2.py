puzzle_file = open('input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
#print(puzzle_input)
# define my help variables
width_of_room = len(puzzle_input[0])
height_of_room = len(puzzle_input)
position_of_guard = ''.join(puzzle_input).find('^')
x_guard = position_of_guard % width_of_room
y_guard = position_of_guard // width_of_room
direction = '^'
puzzle_input[y_guard] = puzzle_input[y_guard].replace('^','.')
guard = (x_guard, y_guard)
guard_start = guard

# initialize the spots visited as an empty set
spots_visited = set((guard, '.'),)
possible_obstructions = set()

# check if the guard is about to leave the room
def is_leaving_the_room(pos):
    x, y = pos
    if direction == '^' and y == 0:
        return True
    elif direction == '>' and x == width_of_room - 1:
        return True
    elif direction == 'v' and y == height_of_room -1:
        return True
    elif direction == '<' and x == 0:
        return True
    return False

# change the direction of the guard
def change_direction():
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

# take a step in the current direction
def take_step(pos):
    x, y = pos
    if direction == '^':
        return (x, y - 1)
    elif direction == '>':
        return (x + 1, y)
    elif direction == 'v':
        return (x, y + 1)
    elif direction == '<':
        return (x - 1, y)
    
# check if the guard is blocked
def is_blocked(pos):
    x, y = pos
    if direction == '^' and puzzle_input[y - 1][x] == '#':
        return True
    elif direction == '>' and puzzle_input[y][x + 1] == '#':
        return True
    elif direction == 'v' and puzzle_input[y + 1][x] == '#':
        return True
    elif direction == '<' and puzzle_input[y][x - 1] == '#':
        return True
    return False



# check if an obstruction put in front of the guard right now would create a loop
def can_loop(guard):
    temp_direction = change_direction()
    temp_guard_with_direction = (guard, temp_direction)
    #print({temp_guard_with_direction,})
    if  {temp_guard_with_direction,} <= spots_visited and take_step(guard) != guard_start:
        return True
    return False    

# include the starting position of the guard in the set of obstructions
# because I am not allowed to put an obstruction there, i want to rule out
# these spots by adding them all in, and subtracting them at the end.

while True:
    # add the current position to the spots visited
    #print(guard)
    #print(direction)
    spots_visited.add((guard,direction),)
    if is_leaving_the_room(guard):
        break
    else:
        if is_blocked(guard):
            direction = change_direction()
            continue
        else:
            if can_loop(guard):
                temp_guard = take_step(guard)
                temp_guard_with_direction = (temp_guard, direction)
                possible_obstructions.add(temp_guard_with_direction)
            guard = take_step(guard)
            continue

print(f'The Guard visited {len(spots_visited)} spots in the room.')
print(f'There are {len(possible_obstructions)} spots \
where i can put an obstruction to create a loop.')
        
# wenn vor mir nicht blockiert ist, und ich schon mal hier war mit der richtung rechts von mir, 
# dann packe die position vor mir in die liste der möglichen Blockaden vor mir 