"""
--- Day 4: Camp Cleanup ---
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""

def __main__():
    counter = []
    with open('day_4_input.txt', 'r') as file:
        for line in file:
            elf_1, elf_2 = line.split(',')
            sections_as_int = list(map(int, elf_1.split('-')))
            sections_of_first_elf = range(sections_as_int[0], sections_as_int[1]+1)
            sections_as_int = list(map(int, elf_2.split('-')))
            sections_of_second_elf = range(sections_as_int[0], sections_as_int[1]+1)
            counter.append(any(item in sections_of_first_elf for item in sections_of_second_elf) or any(item in sections_of_second_elf for item in sections_of_first_elf))
    print(counter.count(True))
    
__main__()