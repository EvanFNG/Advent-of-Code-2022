import pandas as pd

df = pd.read_table('input_files/day5_sample.txt', sep = '\t')

# Use header as first row
df = df.T.reset_index().T.reset_index(drop = True)

df = df.iloc[:, 0].str.split(r"\s+", expand = True, regex = True)

column_list = []

for col_name, col_data in df.items():
    column_list.append([i for i in col_data.tolist() if i != ''])

with open('input_files/day5_sample_moves.txt', 'r') as file:
    move_list = file.read().splitlines()

def read_move(s: str) -> list[int]:
    '''
    Reads a move of the format 'move a from b to c' as [a, b, c]

    a: number to take / of times to repeat
    b: list to take from
    c: list to move to

    Indexing starts at 1, additions and removals are made from
    the beginning of the list.

    Example:
    read_move('move 1 from 2 to 1') -> [1, 2, 1]
    '''

    return [int(i) for i in s if i.isdigit()]

def move(move_list: list[int], crate_list: list[list[str]]) -> list[list[str]]:

    # Copy of crate_list
    # Modify this rather than the input
    result_list = [i.copy() for i in crate_list]

    repeats = move_list[0]
    move_from_index = move_list[1] - 1
    move_to_index = move_list[2] - 1

    return result_list

numerical_moves = [read_move(i) for i in move_list]

print(column_list)
print(move_list)
print(numerical_moves)
print('\n\n')

for i in numerical_moves:
    print(move(move_list = i, crate_list = column_list))