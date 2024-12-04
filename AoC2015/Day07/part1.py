
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day07/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(lines)
puzzle_file.close()
wires ={
    'a': 0
}
for line in puzzle_input:
    line = line.split()
    target = line[-1]
    #check if the target wire is in the dictionary already
    if wires.get(target, '') == '':
        wires.update({target: 0})
    #check what operation to perform
    #check for a gate
    if line[1] == '->':
        #direct assignment from a different wire
        wires.get(line[0],line[0])
        
        wires[target] = wires[line[0]]
        #direct assignment from a value
    #differentiate the gates

print(wires['a'])

test_list = [0]
