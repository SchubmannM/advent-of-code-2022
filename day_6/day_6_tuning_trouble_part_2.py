"""
--- Day 6: Tuning Trouble ---
--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?
"""

def __main__():
    with open('day_6_input.txt', 'r') as file:
        for line in file:
            chars = []
            for pos, char in enumerate(line):
                # Handling the first 4 characters as the list doesnt have enough entries yet
                if len(chars) < 14:
                    chars.append(char)
                else:
                    # We have enough entries -> Check if they are all unique
                    if not len(set(chars)) == len(chars):
                        chars.pop(0)
                        chars.append(char)
                    else:
                        print(pos) # Returning the value before
                        return

__main__()