from string import ascii_lowercase, ascii_uppercase

def split_half(s: str) -> list:
    '''
    Splits a string into two halves.
    Returns: list
    '''

    x = len(s) // 2

    return [s[:x], s[x:]]

def list_shared_elements(l1: list, l2: list) -> list:
    '''
    Returns a list of elements that are shared
    between the two input lists.
    '''

    return list(set(l1) & set(l2))

lower_dict = {letter: value + 1 for value, letter in enumerate(ascii_lowercase)}
upper_dict = {letter: value + 27 for value, letter in enumerate(ascii_uppercase)}

# Merges the two dictionaries.
letter_dict = lower_dict | upper_dict

with open('day3.txt', 'r') as f:
    data = f.read().splitlines()

split_inputs = [split_half(i) for i in data]

common_items = [list_shared_elements(i[0], i[1]) for i in split_inputs]

item_values = [letter_dict[i[0]] for i in common_items]

print(sum(item_values))
