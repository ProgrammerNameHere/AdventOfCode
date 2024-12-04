
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day06/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(lines)
puzzle_file.close()
dimension = 1000
lamps = [[0 for _ in range(dimension)] for _ in range(dimension)]
for line in puzzle_input:
    line =line.split()
    [x_end,y_end] = list(map(int,line.pop().split(',')))
    line.pop()
    [x_start,y_start] = list(map(int,line.pop().split(',')))
    if line.pop(0) == 'turn':
        if line.pop(0) == 'on':
            #turn on
            for x in range(x_start,x_end+1):
                for y in range(y_start,y_end+1):
                    lamps[x][y] += 1
        else:
            #turn off
            for x in range(x_start,x_end+1):
                for y in range(y_start,y_end+1):
                    if lamps[x][y] > 0:
                        lamps[x][y] -= 1
    else:
        #toggle
        for x in range(x_start,x_end+1):
                for y in range(y_start,y_end+1):
                    lamps[x][y] += 2
print(sum(sum(lamps,[])))
