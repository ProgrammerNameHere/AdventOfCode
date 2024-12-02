puzzle_file = open('/Users/moses/Documents/PythonCode/advent_of_code/AoC2024/Day02/input.txt', 'r')
#puzzle_input = puzzle_file.read()
lines = puzzle_file.readlines()
#lines = ["1 2 3 4 5 6 7 8 12\n"]
#print(puzzle_input)
puzzle_file.close()
def is_safe(levels):
    false_level = 0
    number_of_levels = len(levels)
    for j in range(number_of_levels+1):
        #print(f'Aktuelle Liste: {levels}')
        #print(f'Aktueller Index: {j}')
        first_pair_difference = levels[0] - levels[1]
        if first_pair_difference in [1, 2, 3]:
            for i in range(len(levels)-1):
                if levels[i] - levels[i+1] in [1,2,3]:
                    continue
                else:
                    break
            else:
                #print('Safe')
                return True
        elif first_pair_difference in [-1, -2, -3]:
            for i in range(len(levels)-1):
                if levels[i] - levels[i+1] in [-1,-2,-3]:
                    continue
                else:
                    break
            else:
                #print('Safe')
                return True
        
        if j != 0:
            levels.insert(j-1, false_level)
        if j < number_of_levels:
            false_level = levels.pop(j)
    else:
        return False
            

        
        
    
safe_levels = 0
for line in lines:
    line.strip('\n')
    levels = line.split()
    levels_int = list(map(int,levels))
    if is_safe(levels_int):
        safe_levels += 1
print(safe_levels)