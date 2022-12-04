from string import ascii_letters
from functools import reduce
from itertools import zip_longest

def split_half(s: str) -> list:
    '''
    Splits a string into two halves.
    Returns: list
    '''

    x = len(s) // 2

    return [s[:x], s[x:]]

def list_intersect(*args) -> list:
    '''
    Returns a list of elements that are shared
    between the input lists.
    '''
    if len(args) == 1:
        intersect = reduce(lambda x, y: set(x) & set(y), args[0])
    else:
        intersect = reduce(lambda x, y: set(x) & set(y), args)

    return list(intersect)

# From the itertools recipe
# https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

letter_dict = {letter: value + 1 for value, letter in enumerate(ascii_letters)}

with open('input_files/day3.txt', 'r') as f:
    data = f.read().splitlines()

split_inputs = [split_half(i) for i in data]

common_items = [list_intersect(i[0], i[1]) for i in split_inputs]

# Sum of this is solution to part 1
item_values = [letter_dict[i[0]] for i in common_items]

groups = list(grouper(iterable = data, n = 3))

group_common_items = [list_intersect(i) for i in groups]

# Part 2 solution
print(sum([letter_dict[i[0]] for i in group_common_items]))