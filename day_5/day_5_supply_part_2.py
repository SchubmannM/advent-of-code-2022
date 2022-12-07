"""
--- Day 5: Supply Stacks ---
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""
from collections import defaultdict, OrderedDict

STACK_WIDTH = 4
FIRST_STACK = 1

def __main__():
    stacks = defaultdict(list)
    with open('day_5_input.txt', 'r') as file:
        stack_initialised = False
        for line in file:
            if line == '\n':
                continue
            if stack_initialised:
                # Stack is initialised - we have an ordered dict with all boxes in place
                amount_to_move, from_stack, to_stack = map(int, line.replace('move ','').replace(' from ',',').replace(' to ',',').split(','))
                objects_to_move = []
                for x in range(amount_to_move):
                    try:
                        objects_to_move.append(stacks[from_stack].pop())
                    except IndexError:
                        pass
                objects_to_move.reverse()  # Crate picks them up all at once so we want to reverse the order
                stacks[to_stack].extend(objects_to_move)
            else:
                # Not yet initialised -> Fill in the stacks with boxes
                if '[' not in line:
                    stack_initialised = True
                    continue
                    
                if stack_initialised is False:
                    number_of_stacks = int(len(line) / STACK_WIDTH) # Calculate how many columns we have
                    for x in range(0, number_of_stacks+1):
                        try:
                            if line[FIRST_STACK+x*4] != ' ':
                                # As we go top to bottom we insert the boxes at the bottom (0)
                                stacks[x+1].insert(0, line[FIRST_STACK+x*4])
                        except IndexError:
                            pass
    stacks = OrderedDict(sorted(stacks.items(), key=lambda t: t[0]))
    print(stacks)
    print(''.join([str(value[-1]) for value in stacks.values()]))


__main__()