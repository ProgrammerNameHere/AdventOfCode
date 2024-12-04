puzzle_file = open('/Users/moses/Documents//advent_of_code/AoC2024/Day04/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
width = len(puzzle_input[0])
height = len(puzzle_input)
xmas_occurrences = 0
for x in range(width):
    for y in range(height):
        #check if starting letter is 'X'
        if puzzle_input[x][y] == 'X':
            #check the eight possibilities starting on the right and going clockwise
            #right
            if x < width - 3 and puzzle_input[x+1][y] == 'M' and puzzle_input[x+2][y] == 'A' and puzzle_input[x+3][y] == 'S':
                xmas_occurrences += 1
            #right-down
            if x < width - 3 and y < height - 3 and puzzle_input[x+1][y+1] == 'M' and puzzle_input[x+2][y+2] == 'A' and puzzle_input[x+3][y+3] == 'S':
                xmas_occurrences += 1
            #down
            if y < height - 3 and puzzle_input[x][y+1] == 'M' and puzzle_input[x][y+2] == 'A' and puzzle_input[x][y+3] == 'S':
                xmas_occurrences += 1
            #left-down
            if x > 2 and y < height - 3 and puzzle_input[x-1][y+1] == 'M' and puzzle_input[x-2][y+2] == 'A' and puzzle_input[x-3][y+3] == 'S':
                xmas_occurrences += 1
            #left
            if x > 2 and puzzle_input[x-1][y] == 'M' and puzzle_input[x-2][y] == 'A' and puzzle_input[x-3][y] == 'S':
                xmas_occurrences += 1
            #left-up
            if x > 2 and y > 2 and puzzle_input[x-1][y-1] == 'M' and puzzle_input[x-2][y-2] == 'A' and puzzle_input[x-3][y-3] == 'S':
                xmas_occurrences += 1
            #up
            if y > 2 and puzzle_input[x][y-1] == 'M' and puzzle_input[x][y-2] == 'A' and puzzle_input[x][y-3] == 'S':
                xmas_occurrences += 1
            #right-up
            if x < width - 3 and y > 2 and puzzle_input[x+1][y-1] == 'M' and puzzle_input[x+2][y-2] == 'A' and puzzle_input[x+3][y-3] == 'S':
                xmas_occurrences += 1
print(xmas_occurrences)