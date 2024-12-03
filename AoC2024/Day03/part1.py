import re
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2024/Day03/input.txt', 'r')
puzzle_input = puzzle_file.read()
#puzzle_input = puzzle_file.readlines()
#for line in puzzle_input:
#    line.strip('\n')
#print(puzzle_input)
puzzle_file.close()
#find all the correct mul(***,***) instructions
list_of_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", puzzle_input)
#print(mul_list)
sum_of_mul = 0
calculate = True
for instruction in list_of_instructions:
    instruction = instruction.strip("mul()")
    if instruction == "do":
        calculate = True
        continue
    if instruction == "don't":
        calculate = False
        continue
    if calculate:
        (factor1,factor2) = instruction.split(',')
        sum_of_mul += int(factor1) * int(factor2)
print(sum_of_mul)