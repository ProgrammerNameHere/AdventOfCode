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

# initialize the spots visited as an empty set
spots_visited = set()
for y in range(42, 45):
    print(puzzle_input[y][81:84])
print
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


while True:
    # add the current position to the spots visited
    print(guard)
    print(direction)
    spots_visited.add(guard)
    if is_leaving_the_room(guard):
        break
    else:
        if is_blocked(guard):
            direction = change_direction()
            continue
        else:
            guard = take_step(guard)
            continue

print(f'The Guard visited {len(spots_visited)} spots in the room')
        
