with open('input_files/day4.txt', 'r') as f:
    data = f.read().splitlines()

sublists = [i.split(',') for i in data]

def str_to_range(s: str) -> range:
    '''
    Converts a string of the form 'a-b' to range(a, b+1)

    Example:
    str_to_range('8-13') -> range(8, 14)
    '''

    num_list = [int(i) for i in s.split('-')]
    return range(num_list[0], num_list[1] + 1)

def range_overlaps(range_list: list) -> bool:
    '''
    Given a list of two range objects,
    checks to see if either range is fully contained
    within the other.

    Returns: bool

    Examples:
    range_overlaps([range(3, 11), range(4, 7)]) -> True
    range_overlaps([range(8, 13), range(42, 50)]) -> False
    '''

    setlist = [set(i) for i in range_list]

    return ((setlist[0].issubset(setlist[1])) or (setlist[0].issuperset(setlist[1])))

rng_list = [list(map(str_to_range, i)) for i in sublists]

bool_list = [range_overlaps(i) for i in rng_list]

part_one_solution = sum(bool_list)

part_two_solution = sum(map(lambda x: len(set(x[0]) & set(x[1])) > 0, rng_list))
