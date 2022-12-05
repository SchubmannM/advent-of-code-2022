"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""
DRAW = 3
WIN = 6
LOSE = 0

result_values= {'X': LOSE, 'Y': DRAW, 'Z': WIN}
point_values= {'A': 1, 'B': 2, 'C': 3}

def process_game(opp_value, my_value) -> int:
    """
    A Rock 
    B Paper
    C Scissor

    X - Lose
    Y - Draw
    Z - WIN
    """
    
    points = 0
    if opp_value == 'A':
        if my_value == 'X':
            points = point_values.get('C')
        if my_value == 'Y':
            points = point_values.get('A')
        if my_value == 'Z':
            points = point_values.get('B')
    if opp_value == 'B':
        if my_value == 'X':
            points = point_values.get('A')
        if my_value == 'Y':
            points = point_values.get('B')
        if my_value == 'Z':
            points = point_values.get('C')
    if opp_value == 'C':
        if my_value == 'X':
            points = point_values.get('B')
        if my_value == 'Y':
            points = point_values.get('C')
        if my_value == 'Z':
            points = point_values.get('A')

    return points + result_values.get(my_value)

def __main__():
    first_column = []
    second_column = []
    number_of_points = 0
    with open('day_2_input.txt') as file:
        for line in file:
            first_value, second_value = line.split()
            first_column.append(first_value)
            second_column.append(second_value)
    for opp_value, my_value in zip(first_column, second_column):
        number_of_points+=process_game(opp_value, my_value)
    print(f'Total number of points: {number_of_points}')
__main__()
