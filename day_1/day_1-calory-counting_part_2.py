"""
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

def __main__():
    all_elves = []
    with open('day_1_input.txt', 'r') as datafile:
        current_elf = []
        for line in datafile:
            try:
                current_elf.append(int(line))
            except ValueError:
                all_elves.append(current_elf)
                current_elf = []
    
    sum_of_all_elves = []
    for elf in all_elves:
        sum_of_all_elves.append(sum(elf))
    
    top_three_elves = list(sorted(sum_of_all_elves, reverse=True))[:3]

    print(f'Maximum number of calories carried: {sum(top_three_elves)}')


__main__()
