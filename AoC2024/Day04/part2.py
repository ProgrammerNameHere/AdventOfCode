puzzle_file = open('/Users/moses/Documents//advent_of_code/AoC2024/Day04/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
width = len(puzzle_input[0])
height = len(puzzle_input)
x_mas_occurrences = 0
for x in range(width):
    for y in range(height):
        #check if starting letter is 'X'
        if puzzle_input[x][y] == 'A':
            #check for the edge
            if x == 0 or x == width -1 or y == 0 or y == height -1:
                continue
            #check for the proper configuration of letters
            if ((puzzle_input[x-1][y-1] == 'M' and puzzle_input[x+1][y+1] == 'S') or (puzzle_input[x-1][y-1] == 'S' and puzzle_input[x+1][y+1] == 'M')) and ((puzzle_input[x+1][y-1] == 'M' and puzzle_input[x-1][y+1] == 'S') or (puzzle_input[x+1][y-1] == 'S' and puzzle_input[x-1][y+1] == 'M')):
                x_mas_occurrences += 1

print(x_mas_occurrences)