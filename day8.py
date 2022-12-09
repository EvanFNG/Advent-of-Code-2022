with open('input_files/day8.txt', 'r') as f:
    text = f.read().splitlines()
    data = [[int(y) for y in list(x)] for x in text]

# Running total of visible trees
viz_count = 0

def neighbor_coords(start: list[int]) -> list[list[int]]:
    '''
    Returns the coordinates of the neighbors of start.

    >>> neighbor_coords([1, 3])
    [[2, 3], [0, 3], [1, 2], [1, 4]]
    '''
    
    x, y = start
    return [[x+1, y], [x-1, y], [x, y-1], [x, y+1]]

def tree_neighbors_adjacent(point_index: list[int], arr: list[list[int]]) -> list[int]:
    '''
    Returns a tree's adjacent neighbors given its index
    and the 2D array it's contained in.
    Does not include diagonals.

    >>> tree_neighbors_adjacent([1, 1], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [2, 4, 6, 8]
    '''

    coords = neighbor_coords(point_index)
    neighbors = []

    for coord in coords:
        try:
            # Negative coordinates should be tossed
            if (coord[0] >= 0) and (coord[1] >= 0):
                neighbors.append(arr[coord[0]][coord[1]])
        except IndexError:
            pass

    return neighbors

def tree_neighbors_all(point: list[int], arr: list[list[int]]) -> list[list[int]]:
    '''
    Similar to tree_neighbors_adjacent,
    but returns the entire neighboring column and row.

    >>> tree_neighbors_all([1, 1], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[4], [6], [2], [8]]
    '''

    x, y = point

    l = [[i for i in arr[x][:y]], [j for j in arr[x][y+1:]]]

    col1 = []
    col2 = []

    for row in arr[:x]:
            col1.append(row[y])

    l.append(col1)

    for row in arr[x+1:]:
        col2.append(row[y])
    
    l.append(col2)

    l = [i for i in l if i != []]

    return l

data_length = len(data)

# viz_count will be the answer to part 1
for row_index, row in enumerate(data):
    for tree_index, tree in enumerate(row):
        x, y = [row_index, tree_index]
        neighbors = [max(i) for i in tree_neighbors_all([x, y], data)]
        viz_bool = any([tree > i for i in neighbors])
        if any(
            [
                viz_bool,
                row_index in [0, data_length - 1],
                tree_index in [0, data_length - 1]
            ]
        ):
            viz_count += 1