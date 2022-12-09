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