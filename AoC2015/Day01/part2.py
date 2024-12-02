puzzle_file = open('/Users/moses/Documents/PythonCode/advent_of_code/AoC2015/Day01/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(puzzle_input)
puzzle_file.close()
floor = 0
position = 0
#part1 Solution
for char in puzzle_input:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    position += 1
    if floor == -1:
        print(position)
        break
print(floor)