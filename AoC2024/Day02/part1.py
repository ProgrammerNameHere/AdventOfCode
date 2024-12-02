puzzle_file = open('/Users/moses/Documents/PythonCode/advent_of_code/AoC2024/Day02/input.txt', 'r')
#puzzle_input = puzzle_file.read()
lines = puzzle_file.readlines()
#print(puzzle_input)
puzzle_file.close()
def is_safe(levels):
    first_pair_difference = levels[0] - levels[1]
    if first_pair_difference >= 1 and first_pair_difference <= 3:
        for i in range(len(levels)-1):
            if levels[i] - levels[i+1] in [1,2,3]:
                continue
            else:
                return False
        else:
            return True
    elif first_pair_difference <= -1 and first_pair_difference >= -3:
        for i in range(len(levels)-1):
            if levels[i] - levels[i+1] in [-1,-2,-3]:
                continue
            else:
                return False
        else:
            return True
    else:
        return False
        
        
    
counter = 0
for line in lines:
    line.strip('\n')
    levels = line.split()
    levels_int = list(map(int,levels))
    if is_safe(levels_int):
        counter += 1
print(counter)