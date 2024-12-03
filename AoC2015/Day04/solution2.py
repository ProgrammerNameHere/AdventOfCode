import hashlib
import re
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day04/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(lines)
puzzle_file.close()
number = 0
done = False 
while not done:
    hash_seed = puzzle_input + str(number)
    result = hashlib.md5(hash_seed.encode('utf-8'))
    ###print(hash_seed)
    ##print(number)
    #print(result.hexdigest())
    if re.findall('^0{6,}', result.hexdigest()) != []:
        print(number)
        done = True
    number += 1