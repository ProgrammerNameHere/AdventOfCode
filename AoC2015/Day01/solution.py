puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day01/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(puzzle_input)
puzzle_file.close()
#initialize my counters
floor = 0
position = 0
#check every character and if it's '(' increase the floor, if not decrease it
for char in puzzle_input:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    position += 1
    #print the steps in which the basement (floor -1) is entered
    if floor == -1:
        print(position)
print(floor)
