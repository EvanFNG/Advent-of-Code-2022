import re

column_list = [
    ['[W]', '[L]', '[S]'],
    ['[Q]', '[N]', '[T]', '[J]'],
    ['[J]', '[F]', '[H]', '[C]', '[S]'],
    ['[B]', '[G]', '[N]', '[W]', '[M]', '[R]', '[T]'],
    ['[B]', '[Q]', '[H]', '[D]', '[S]', '[L]', '[R]', '[T]'],
    ['[L]', '[R]', '[H]', '[F]', '[V]', '[B]', '[J]', '[M]'],
    ['[M]', '[J]', '[N]', '[R]', '[W]', '[D]'],
    ['[J]', '[D]', '[N]', '[H]', '[F]', '[T]', '[Z]', '[B]'],
    ['[T]', '[F]', '[B]', '[N]', '[Q]', '[L]', '[H]']
]

with open('input_files/day5_moves.txt', 'r') as file:
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
    regex = re.compile(r"(\d{1,2})")
    return [int(i) for i in regex.findall(s)]

def move(move_list: list[int], crate_list: list[list[str]]) -> list[list[str]]:

    # Copy of crate_list
    # Modify this rather than the input
    result_list = [i.copy() for i in crate_list]

    # Number of iterations
    repeats = move_list[0]

    # Index of list to take from is 1 less than the second element of move_list
    move_from_index = move_list[1] - 1

    # Index of list to move to is 1 less than the third element of move_list
    move_to_index = move_list[2] - 1

    for _ in range(repeats):

        # Item to be moved
        content = result_list[move_from_index][0]
        
        # Insert the content at the beginnig of the correct list
        result_list[move_to_index].insert(0, content)

        # Remove the content from the list taken from
        result_list[move_from_index].pop(0)

    return result_list

numerical_moves = [read_move(i) for i in move_list]

print(column_list)
print('\n\n')

for i in numerical_moves:
    column_list = move(move_list = i, crate_list = column_list)

part_one_string = ''

for lst in column_list:
    part_one_string += lst[0][1]