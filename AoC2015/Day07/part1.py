
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day07/test_input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(lines)
puzzle_file.close()
wires ={

}
for line in puzzle_input:
    #print(wires)
    print(line)
    line = line.split(' -> ')
    target = line[1]
    input = line[0].split()
    line_rebuild = ' -> '.join(line)
    # direct input or input from wire
    if len(input) == 1:

        if wires.get(input[0], True) and not input[0].isdigit():
            puzzle_input.append(line_rebuild)
            break
        source = wires.get(input[0], int(input[0]))
        wires.update({target: source})
    elif len(input) == 2: # NOT gate
        #if the wire is not active yet, add this instruction to the end of the list
        if wires.get(input[1], None) == None:
            puzzle_input.append(line_rebuild)
            break
        wires.update({target: (~ wires[input[1]])})
    else: # all other logic gates
        gate = input[1]
        left_of_gate, right_of_gate = input[0], input[2]
        if gate == 'AND':
            if wires.get(left_of_gate, True) == True or wires.get(right_of_gate, True) == True:
                puzzle_input.append(line_rebuild)
                break
            wires.update({target: (wires[left_of_gate] & wires[right_of_gate])})
        elif gate == 'OR':
            if wires.get(left_of_gate, True) == True or wires.get(right_of_gate, True) == True:
                puzzle_input.append(line_rebuild)
                break
            wires.update({target: (wires[left_of_gate] | wires[right_of_gate])})
        elif gate == 'LSHIFT':
            if wires.get(left_of_gate, True) == True:
                puzzle_input.append(line_rebuild)
                break
            wires.update({target: (wires[left_of_gate] << int(right_of_gate))})
        elif gate == 'RSHIFT':
            if wires.get(left_of_gate, True) == True:
                puzzle_input.append(line_rebuild)
                break
            wires.update({target: (wires[left_of_gate] >> int(right_of_gate))})

print(wires)
