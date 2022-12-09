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

        if self.location() == 'Inner':

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

        else:
            return 0

# Running total of visible trees
visibile_count = 0

scores = []

for row_index, row in enumerate(data):
    for tree_index, tree in enumerate(row):

        curr_tree = Tree(coords = [row_index, tree_index], arr = data)

        # Part One
        neighbors = curr_tree.neighbors_all()
        neighbors_max = [max(i) for i in neighbors]
        visible = any([curr_tree.height() > i for i in neighbors_max])

        if visible or (curr_tree.location() != 'Inner'):
            visibile_count += 1

        # Part Two
        scores.append(curr_tree.scenic_score())

part_two_solution = max(scores)

print(part_two_solution)