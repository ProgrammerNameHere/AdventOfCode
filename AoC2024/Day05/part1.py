puzzle_file = open('input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
#print(puzzle_input)
seperator = puzzle_input.index('')
#split the input into rules and updates
rules_list = puzzle_input[:seperator]
updates_list = list(map(lambda x: x.split(','),puzzle_input[seperator + 1:]))
rules = {}
ordered_updates = []
sum_of_middle = 0

#collect all the rules in a dictionary of sets
for rule in rules_list:
    # seperate the rule into the requirement and the page
    [requirement, page] = rule.split('|')
    if rules.get(page) == None: # if the page has no rules yet, add the current requirement
        rules.update({page: {requirement}})
    else: # if the page has a requirement, update it with the current requirements
        rules[page].add(requirement)

# check if an update is in the right order and return True/False
def is_in_right_order(update):
    # initiate the necessary variables
    pages_in_this_update = set(update)
    printed = set()

    # check every pages requirements against the already printed pages
    for page in update:
        relevant_rules = rules[page] & pages_in_this_update
        # if yes: print the current page and check the next page
        if relevant_rules <= printed:
            printed.add(page)
        else: # if no: return False
            return False
    return True #if the loop arrives here, the update is in the correct order and can be printed as-is

# filter the updates for the ones that are in order
ordered_updates = filter(is_in_right_order, updates_list)

# sum up the ordered updates
for update in ordered_updates:
    sum_of_middle += int(update[len(update)//2])

# print the solution to part1
print(f'The ordered updates sum to: {sum_of_middle}')