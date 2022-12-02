with open('input_files/day2.txt', 'r') as f:
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

    if translation in round_result_dict:

        return round_result_dict[translation]

    # Handles case when the opposite order of an existing key is passed in,
    # e.g. ('Paper', 'Rock') instead of ('Rock', 'Paper')
    else:
        return round_result_dict[translation[::-1]][::-1]

scores = [rock_paper_scissors(i) for i in data]

# Sum of this is the asnwer to part 1
p2_scores = [i[1] for i in scores]

def p2_score(p1_move: str, desired_outcome: str) -> int:
    '''
    Determines the correct response from Player 2 according to Player 1's move
    and the code in column 2 of data.
    Returns player 2's score.
    '''

    # A: Rock, B: Paper, C: Scissors
    shape_values = {'A': 1, 'B': 2, 'C': 3}

    # X: Lose, Y: Draw, Z: Win
    outcome_values = {'X': 0, 'Y': 3, 'Z': 6}

    match desired_outcome:

        # Draw
        case 'Y':

            return outcome_values[desired_outcome] + shape_values[p1_move]

        # Win
        case 'Z':

            if p1_move == 'A':
                return outcome_values[desired_outcome] + shape_values['B']

            elif p1_move == 'B':
                return outcome_values[desired_outcome] + shape_values['C']

            else:
                return outcome_values[desired_outcome] + shape_values['A']

        # Lose
        case 'X':

            if p1_move == 'A':
                return outcome_values[desired_outcome] + shape_values['C']

            elif p1_move == 'B':
                return outcome_values[desired_outcome] + shape_values['A']

            else:
                return outcome_values[desired_outcome] + shape_values['B']

print(sum([p2_score(i[0], i[1]) for i in data]))