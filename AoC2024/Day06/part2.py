import time

puzzle_file = open('test_input.txt', 'r')
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
direction = puzzle_input[y_guard][x_guard]
guard_start = (x_guard, y_guard)
guard = (x_guard, y_guard)

# initialize the spots visited as an empty set and
spots_visited = set()
spots_visited_with_direction = set((guard, '.'),)
possible_obstructions = set()

# check if the guard is about to leave the room
def is_leaving_the_room(pos, facing_direction):
    x, y = pos
    if facing_direction == '^' and y == 0:
        return True
    elif facing_direction == '>' and x == width_of_room - 1:
        return True
    elif facing_direction == 'v' and y == height_of_room -1:
        return True
    elif facing_direction == '<' and x == 0:
        return True
    return False

# change the direction of the guard
def change_direction(current_direction):
    if current_direction == '^':
        return '>'
    elif current_direction == '>':
        return 'v'
    elif current_direction == 'v':
        return '<'
    elif current_direction == '<':
        return '^'

# take a step in the current direction
def take_step(pos, step_direction):
    x, y = pos
    if step_direction == '^':
        return (x, y - 1)
    elif step_direction == '>':
        return (x + 1, y)
    elif step_direction == 'v':
        return (x, y + 1)
    elif step_direction == '<':
        return (x - 1, y)
    
# check if the guard is blocked
def is_blocked(pos, block_direction):
    x, y = pos
    if block_direction == '^' and puzzle_input[y - 1][x] == '#':
        return True
    elif block_direction == '>' and puzzle_input[y][x + 1] == '#':
        return True
    elif block_direction == 'v' and puzzle_input[y + 1][x] == '#':
        return True
    elif block_direction == '<' and puzzle_input[y][x - 1] == '#':
        return True
    return False



# check if an obstruction put in front of the guard right now would create a loop
def can_loop(guard, loop_direction):
    temp_direction = change_direction(loop_direction)
    #print({temp_guard_with_direction,})
    if  {(guard, temp_direction),} <= spots_visited_with_direction or take_step(guard, loop_direction) == guard_start:
        return True
    return False    

# include the starting position of the guard in the set of obstructions
# because I am not allowed to put an obstruction there, i want to rule out
# these spots by adding them all in, and subtracting them at the end.

while True:
    # add the current position to the spots visited
    # print(guard)
    # print(direction)
    # x_current, y_current = guard
    # vision_range = 1
    # for y in range(y_current - vision_range//2, y_current + vision_range//2 + 1):
    #     print(puzzle_input[y][x_current - vision_range//2:x_current + vision_range//2 + 1])
    # time.sleep(.2)
    spots_visited.add((guard),)
    spots_visited_with_direction.add((guard,direction),)
    if is_leaving_the_room(guard, direction):
        break
    else:
        if is_blocked(guard, direction):
            direction = change_direction(direction)
            # print('Obstacle Detected')

            continue
        else:
            if can_loop(guard, direction):
                # print('Loop Detected')
                temp_guard = take_step(guard, direction)
                possible_obstructions.add(temp_guard,)
            # print('Stepping Forward')
            guard = take_step(guard,direction)
            
            continue

print(f'The Guard visited {len(spots_visited)} spots in the room.')
print(f'There are {len(possible_obstructions)} spots \
where i can put an obstruction to create a loop.')
print(possible_obstructions)
        
# wenn vor mir nicht blockiert ist, und ich schon mal hier war mit der richtung rechts von mir, 
# dann packe die position vor mir in die liste der möglichen Blockaden vor mir 