import re
#open the input file and read the contents into a string
puzzle_file = open('input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
puzzle_input.sort()
#print(lines)
puzzle_file.close()

#special Characters: \\ = \, \" = ", \xXX = '
sum_of_characters_in_code = 0
sum_of_characters_in_memory = 0

for string in puzzle_input:
    # account for the " at the start and the end of the string
    print(f'Starting string: {string}')
    sum_of_characters_in_code += 2
    string = string[1:-1]
    sum_of_characters_in_code += len(re.findall(r"\\|\"", string))
    
    sum_of_characters_in_code += 3 * len(re.findall(r"x[0-9a-f]{2}", string))
    print('test2')
    #print(string)
    2                                     
    sum_of_characters_in_memory += len(string)
    sum_of_characters_in_code += len(string)
    special = False

    
            
print(f'Sum of all characters in code: {sum_of_characters_in_code}')
print(f'Sum of all characters in memory: {sum_of_characters_in_memory}')
print(f'The difference is therefore: {sum_of_characters_in_code - sum_of_characters_in_memory}')
    