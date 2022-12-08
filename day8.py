with open('input_files/day8_sample.txt', 'r') as f:
    text = f.read().splitlines()
    data = [[int(y) for y in list(x)] for x in text]

# Initial count formula
viz_count = 2 * (len(data[0]) + len(data) - 2)

for i in data:
    print(*i)

print('\n')

def neighbor_coords(start: list[int]) -> list[list[int]]:
    '''
    Returns the coordinates of the neighbors of start.

    >>> neighbor_coords([1, 3])
    [[2, 3], [0, 3], [1, 2], [1, 4]]
    '''
    
    x, y = start
    return [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]

def tree_neighbors(point_index: list[int], arr: list[list[int]]) -> list[int]:
    '''
    Returns a tree's neighbors given its index
    and the 2D array it's contained in.

    >>> tree_neighbors([1, 1], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [2, 4, 6, 8]
    '''

    coords = neighbor_coords(point_index)
    neighbors = []

    


# def count_visible_trees(arr: list[list[int], list[int], list[int]]) -> int:
#     init_count = 0

#     for rows in arr[:2]:
#         pass




# for row_index, row in enumerate(data):
#     # Determine the three arrays of trees to check
#     if row_index == 0:
#         tree_lists = [row, data[row_index+1], data[row_index+2]]
#     elif row_index == len(data):
#         tree_lists = [data[-3], data[-2], row]
#     else:
#         tree_lists = [data[row_index-1], row, data]



print(neighbor_coords([0,0]))