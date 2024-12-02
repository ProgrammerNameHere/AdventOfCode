puzzle_file = open('/Users/moses/Documents/PythonCode/advent_of_code/AoC2024/Day01/input.txt', 'r')
puzzle_input = puzzle_file.read()
#print(puzzle_input)
puzzle_file.close()
locations1 = []
locations2 = []
sum_of_differences = 0
lines = puzzle_input.splitlines()
#print(lines)
for line in lines:
    location_ids = line.split()
    locations1.append(location_ids[0])
    locations2.append(location_ids[1])
locations1.sort()
locations2.sort()
for (location1, location2) in zip(locations1, locations2):
    sum_of_differences += abs(int(location1)-int(location2))
print(sum_of_differences)