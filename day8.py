with open('input_files/day8.txt', 'r') as f:
    text = f.read().splitlines()
    data = [[int(y) for y in list(x)] for x in text]

class Tree:

    def __init__(self, coords: list[int], arr: data = list[list[int]]) -> None:
        self.coords = coords
        self.arr = arr

        # Assume square array
        self.arr_len = len(arr) * len(arr[0])
        self.row_len = len(arr[0])
        self.max_index = self.row_len - 1
    
    def __repr__(self) -> str:
        x, y = self.coords
        return f'{self.coords}: {self.arr[x][y]}'

    def height(self) -> int:
        x, y = self.coords
        return self.arr[x][y]

    def location(self) -> str:
        '''
        One of:
            Top-Left, Top-Right,
            Bottom-Left, Bottom-Right,
            Outer-Left, Outer-Right,
            Outer-Top, Outer-Bottom,
            Inner
        '''

        if self.coords == [0, 0]:
            return 'Top-Left'

        elif self.coords == [0, self.max_index]:
            return 'Top-Right'

        elif self.coords == [self.max_index, 0]:
            return 'Bottom-Left'

        elif self.coords == [self.max_index, self.max_index]:
            return 'Bottom-Right'

        elif (self.coords[0] in range(1, self.row_len)) and (self.coords[1] == 0):
            return 'Outer-Left'

        elif (self.coords[0] in range(1, self.row_len)) and (self.coords[1] == self.max_index):
            return 'Outer-Right'

        elif (self.coords[0] == 0) and (self.coords[1] in range(1, self.row_len)):
            return 'Outer-Top'

        elif (self.coords[0] == self.max_index) and (self.coords[1] in range(1, self.row_len)):
            return 'Outer-Bottom'

        else:
            return 'Inner'

    def neighbors_all(self) -> list[list[int]]:

        x, y = self.coords
        l = [[i for i in self.arr[x][:y]], [j for j in self.arr[x][y+1:]]]

        col1 = []
        col2 = []

        for row in self.arr[:x]:
                col1.append(row[y])

        l.append(col1)

        for row in self.arr[x+1:]:
            col2.append(row[y])
        
        l.append(col2)

        l = [i for i in l if i != []]

        return l

    def scenic_score(self):

        neighbors = self.neighbors_all()
        h = self.height()

        def tally(height: self.height(), trees: list) -> int:

            score = 0
            for tree in trees:
                score += 1
                if height <= tree:
                    break

            return score

        match self.location():

            case 'Inner':
                row_left = neighbors[0]
                row_right = neighbors[1]
                col_up = neighbors[2]
                col_down = neighbors[3]

                row_left.reverse()
                col_up.reverse()

                trees = [row_left, row_right, col_up, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(height = self.height(), trees = tree_list)

                return total

            case 'Top-Left':
                row_right = neighbors[0]
                col_down = neighbors[1]

                trees = [row_right, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Top-Right':
                row_left = neighbors[0]
                col_down = neighbors[1]

                row_left.reverse()

                trees = [row_left, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Bottom-Left':
                row_right = neighbors[0]
                col_up = neighbors[1]

                col_up.reverse()
                trees = [row_right, col_up]

                total = 1
                
                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Bottom-Right':
                row_left = neighbors[0]
                col_up = neighbors[1]

                row_left.reverse()
                col_up.reverse()

                trees = [row_left, col_up]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Outer-Left':
                row_right = neighbors[0]
                col_up = neighbors[1]
                col_down = neighbors[2]

                col_up.reverse()

                trees = [row_right, col_up, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Outer-Right':
                row_left = neighbors[0]
                col_up = neighbors[1]
                col_down = neighbors[2]

                row_left.reverse()
                col_up.reverse()

                trees = [row_left, col_up, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Outer-Top':
                row_left = neighbors[0]
                row_right = neighbors[1]
                col_down = neighbors[2]

                row_left.reverse()

                trees = [row_left, row_right, col_down]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case 'Outer-Bottom':
                row_left = neighbors[0]
                row_right = neighbors[1]
                col_up = neighbors[2]

                row_left.reverse()
                col_up.reverse()

                trees = [row_left, row_right, col_up]

                total = 1

                for tree_list in trees:
                    total *= tally(self.height(), tree_list)

                return total

            case _:
                return 0

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
    Always returns in order [left, right, up, down]

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
        neighbors = tree_neighbors_all([x, y], data)
        neighbors_max = [max(i) for i in neighbors]
        viz_bool = any([tree > i for i in neighbors_max])

        if any(
            [
                viz_bool,
                row_index in [0, data_length - 1],
                tree_index in [0, data_length - 1]
            ]
        ):
            viz_count += 1

scores = []

for row_index, row in enumerate(data):
    for tree_index, tree in enumerate(row):
        curr_tree = Tree(coords = [row_index, tree_index], arr = data)
        scores.append(curr_tree.scenic_score())

part_two_solution = max(scores)