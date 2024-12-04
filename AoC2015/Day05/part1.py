import re
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day05/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
nice_lines = 0
print(len(puzzle_input))
for line in puzzle_input:
    print(line)
    if  re.search(r'(.)\1+', line) != None and re.search('.*[aeiou].*[aeiou].*[aeiou].*', line) != None and re.search ('ab|cd|pq|xy', line) == None:
        nice_lines += 1
print(nice_lines)

