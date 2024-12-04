import hashlib
import re
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day04/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(lines)
puzzle_file.close()
number = 0
done = False 
for line in puzzle_input:
    print(line)
    if  re.search(r'(..).*(\1)', line) != None and re.search(r'(.).(\1)', line) != None:
        nice_lines += 1
print(nice_lines)