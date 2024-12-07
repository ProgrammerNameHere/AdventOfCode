
#open the input file and read the contents into a string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day07/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
puzzle_input.sort()
#print(lines)
puzzle_file.close()

max_bound = 65536
wires ={
}
reverse_puzzle_input = list(map(lambda x: x[::-1], puzzle_input))
reverse_puzzle_input.sort()
puzzle_input = list(map(lambda x: x[::-1], reverse_puzzle_input))

def make_positive(num):
    if abs(num) > 65535:
        num %= 65535
    if num < 0:
        return num + max_bound
    return num

for line in puzzle_input:
    #print(wires)
    #print(line)
    line = line.split(' -> ')
    target = line[1]
    input = line[0].split()
    line_rebuild = ' -> '.join(line)
    # direct input or input from wire
    if len(input) == 1:
        #if the input wire is not active, add this instruction to the end of the list and keep going with the next instruction
        if wires.get(input[0]) == None and not input[0].isdigit():
            puzzle_input.append(line_rebuild)
            continue
        wires.update({target: make_positive(int(wires.get(input[0], input[0])))})
    elif len(input) == 2: # NOT gate
        #if the input wire is not active, add this instruction to the end of the list and keep going with the next instruction
        if wires.get(input[1]) == None:
            puzzle_input.append(line_rebuild)
            continue
        wires.update({target: make_positive(~ wires[input[1]])})
    else: # all other logic gates
        gate = input[1]
        left_of_gate, right_of_gate = input[0], input[2]
        if gate == 'AND':
            #if either of the input wires is not active, add this instruction to the end of the list and keep going with the next instruction
            if (wires.get(left_of_gate) == None and not left_of_gate.isdigit()) or wires.get(right_of_gate) == None:
                puzzle_input.append(line_rebuild)
                continue
            wires.update({target: make_positive(int(wires.get(left_of_gate, left_of_gate)) & wires[right_of_gate])})
        elif gate == 'OR':
            #if either of the input wires is not active, add this instruction to the end of the list and keep going with the next instruction
            if wires.get(left_of_gate) == None or wires.get(right_of_gate) == None:
                puzzle_input.append(line_rebuild)
                continue
            wires.update({target: make_positive(wires[left_of_gate] | wires[right_of_gate])})
        elif gate == 'LSHIFT':
            #if the input wire is not active, add this instruction to the end of the list and keep going with the next instruction
            if wires.get(left_of_gate) == None:
                puzzle_input.append(line_rebuild)
                continue
            wires.update({target: make_positive(wires[left_of_gate] << int(right_of_gate))})
        elif gate == 'RSHIFT':
            #if the input wire is not active, add this instruction to the end of the list and keep going with the next instruction
            if wires.get(left_of_gate) == None:
                puzzle_input.append(line_rebuild)
                continue
            wires.update({target: make_positive(wires[left_of_gate] >> int(right_of_gate))})

print(wires)
