puzzle_file = open('/Users/moses/Documents//advent_of_code/AoC2024/Day05/input.txt', 'r')
puzzle_input = puzzle_file.read().splitlines()
#print(puzzle_input)
puzzle_file.close()
#print(puzzle_input)
seperator = puzzle_input.index('')
#split the input into rules and updates
rules_list = puzzle_input[:seperator]
updates_list = list(map(lambda x: x.split(','),puzzle_input[seperator + 1:]))

# initialize all my variables
rules = {}
ordered_updates = []
unordered_updates = []
fixed_updates = []
sum_of_middle_ordered = 0
sum_of_middle_fixed = 0

#collect all the rules in a dictionary of sets
for rule in rules_list:
    # seperate the rule into the requirement and the page
    [requirement, page] = rule.split('|')
    if rules.get(page) == None: # if the page has no rules yet, add the current requirement
        rules.update({page: {requirement}})
    else: # if the page has a requirement, update it with the current requirements
        rules[page].add(requirement)

#print(rules)

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

# returns the given update in the correct order
def fix_update(update):

    pages_to_be_printed = set(update)
    printed = set()
    relevant_rules = {}
    fixed_update = []
    # create a subset of the relevant rules
    for page in pages_to_be_printed:
        relevant_rules.update({page: rules[page] & pages_to_be_printed})
    # keep going until all pages are printed
    while len(update) > len(printed):
        # check every page one after the other to optimize
        for page in pages_to_be_printed:
            # check if the required pages for the current page have already been printed
            if relevant_rules[page] <= printed:
                printed.add(page) # add the current page to the printed ones
                fixed_update.append(page) # add the current page to the fixed_update
                pages_to_be_printed.remove(page) # remove the page, so it doesn't get added again
                break
                

    return fixed_update
        

# filter the updates for the ones that are in order and the ones that are not
ordered_updates = filter(is_in_right_order, updates_list)
unordered_updates = filter(lambda x:not is_in_right_order(x), updates_list)

# fix all unordered updates and put them into fixed_updates
for update in unordered_updates:
    fixed_updates.append(fix_update(update))

# sum up the ordered updates
for update in ordered_updates:
    sum_of_middle_ordered += int(update[len(update)//2])

# sum up the fixed updates
for update in fixed_updates:
    sum_of_middle_fixed += int(update[len(update)//2])
# print the solutions to part1 and part 2
print(f'The ordered updates sum to: {sum_of_middle_ordered}')
print(f'The fixed updates sum to: {sum_of_middle_fixed}')

            
    


