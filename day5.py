import pandas as pd

df = pd.read_table('input_files/day5_sample.txt', sep = '\t')

# Use header as first row
df = df.T.reset_index().T.reset_index(drop = True)

df = df.iloc[:, 0].str.split(r"\s+", expand = True, regex = True)

column_list = []

for col_name, col_data in df.items():
    column_list.append(col_data.tolist())

with open('input_files/day5_sample_moves.txt', 'r') as file:
    move_list = file.read().splitlines()

def read_move(s: str) -> list:
    '''
    Reads a move of the format 'move a from b to c' as [a, b, c]

    a: number to take
    b: list to take from
    c: list to move to

    Indexing starts at 1, additions and removals are made from
    the beginning of the list.

    Example:
    read_move('move 1 from 2 to 1') -> [1, 2, 1]
    '''

    return [int(i) for i in s if i.isdigit()]

numerical_moves = [read_move(i) for i in move_list]

def make_move(move_list: list, crate_list: list) -> list:

    new_list = [i.copy() for i in crate_list]
    num_to_take = move_list[0]
    move_from = move_list[1] - 1
    move_to = move_list[2] - 1

    content = crate_list[move_from][:num_to_take]

    new_list[move_to][:num_to_take] = content
    new_list[move_from][:num_to_take] = ''

    for _ in range(num_to_take):
        new_list[move_from].insert(0, '')

    return new_list

parsed_moves = [read_move(i) for i in move_list]