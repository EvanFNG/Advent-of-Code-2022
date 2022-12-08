with open('input_files/day8_sample.txt', 'r') as f:
    text = f.read().splitlines()
    data = [[int(y) for y in list(x)] for x in text]

# Initial count formula
# viz_count = 2 * (len(data[0]) + len(data) - 2)
viz_count = 0

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

    for coord in coords:
        try:
            # Negative coordinates should be tossed
            if (coord[0] >= 0) and (coord[1] >= 0):
                neighbors.append(arr[coord[0]][coord[1]])
        except IndexError:
            pass

    return neighbors

def tree_neighbors_2(point: list[int], arr: list[list[int]]) -> list[list[int]]:

    x, y = point
    self = arr[x][y]

    l = [[i for i in arr[x]]]

    col = []

    for row in arr:
        col.append(row[y])
    
    l.append(col)

    l[0].pop(y)
    l[1].pop(y)

    return l

    

print(tree_neighbors_2([4, 4], data))