import functools

# Sample

with open('input_files/day_2_sample.txt', 'r') as f:
    data = [i.split(' ') for i in f.read().splitlines()]

def rock_paper_scissors(move_list: list) -> tuple:
    '''
    Determines the winner of a Rock, Paper, Scissors game
    and returns a score tuple

    Each Shape is worth the following:

    Rock: 1
    Paper: 2
    Scissors: 3

    Each Outcome is worth the following:

    Lose: 0
    Draw: 3
    Win: 6

    The returned tuple contains the sum of points for each player.

    Move list will be trasnslated using the p1_dict and p2_dict dictionaries.

    Examples:

    rock_paper_scissors(['B', 'X']) returns (8, 1)
    rock_paper_scissors(['C', 'Z']) returns (6, 6)
    rock_paper_scissors(['C', 'X']) returns (3, 7)
    '''

    p1_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
    p2_dict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

    round_result_dict = {
        ('Rock', 'Rock'): (4, 4),
        ('Rock', 'Paper'): (1, 8),
        ('Rock', 'Scissors'): (7, 3),
        ('Paper', 'Paper'): (5, 5),
        ('Paper', 'Scissors'): (2, 9),
        ('Scissors', 'Scissors'): (6, 6)
    }

    translation = (p1_dict[move_list[0]], p2_dict[move_list[1]])

    return round_result_dict[translation]

result = functools.reduce(lambda x, y: x[-1] + y[-1], [(1, 8), (2, 9)])

print(result)

for i in data:
    print(rock_paper_scissors(i))