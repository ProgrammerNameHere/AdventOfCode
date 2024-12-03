#open the input file and read the contents into a list of string
puzzle_file = open('/Users/moses/Documents/advent_of_code/AoC2015/Day02/input.txt', 'r')
lines = puzzle_file.read().splitlines()
#print(lines)
puzzle_file.close()
paper_needed = 0
ribbon_needed = 0
#prepare the input so it is a list of a list of numbers
for line in lines:
    lines[lines.index(line)] = list(map(int,line.split('x')))
#print(lines)

for sides in lines:
    sides.sort()
    [height, width, length] = sides
    face1 = height*width
    face2 = width*length
    face3 = length*height
    paper_needed += 2*face1 + 2*face2 + 2*face3 + min(face1,face2,face3)
    ribbon_needed += 2*sides[0] + 2 * sides[1] + height * width * length
print(paper_needed)
print(ribbon_needed)