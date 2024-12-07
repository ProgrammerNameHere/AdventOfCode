puzzle_file = open('./input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
# define global variables
calibration_result = 0

def is_solvable(test, calculation, rolling_total=0)
    if calculation == []:
        if rolling_total == test:
            return True
        else:
            return False
    
    

# check each calibration if it is solvable
# and if so, add the value to the
# calibration result
for calculation in puzzle_input:
    test_value, equation = calculation.split(':')
    numbers_in_equation = equation.strip().split()
    
    if is_solvable(test_value, numbers_in_equation):
        calibration_result += test_value




if __name__ == '__main__':

    print(calibration_result)
