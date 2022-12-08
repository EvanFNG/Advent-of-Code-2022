class File:
    def __init__(self, size: str, name: str):
        self.size = size
        self.name = name

    def __repr__(self) -> str:
        return f''
    
class Directory:
    def __init__(self, name: str, parent: 'Directory' = None):
        self.name = name
        self.children = []
        self.parent = parent

    def add_children(self, node: 'Directory') -> None:
        self.children.append(node)

    def __repr__(self) -> str:
        return self.name

class State:
    def __init__(self, root):
        self.curr: Directory = root
        self.root: Directory = root

    def __repr__(self) -> str:
        return self.curr

with open('input_files/day6_sample.txt', 'r') as f:
    data = f.read().splitlines()

print(data)

# for line in data:
#     splt = line.split(' ')

#     if (splt[0] == '$') and (splt[1] == 'cd'):

#         new_parent = Directory(splt[2])
#         dir_ls.append(new_parent)

def cd(state: State, arg: str) -> None:
    if arg == '..':
        state.curr = state.curr.parent
    elif arg == '/':
        state.curr = state.root
    else:
        for child in state.curr.children:
            if isinstance(child, Directory) and child.name == arg:
                state.curr == child

def process_line(state, line: str):
    chars = line.split(' ')

    if chars[0] == '$':
        command = chars[1]
        if command == 'cd':
            arg = chars[2]
            cd(state = state, arg = arg)
    else:
        pass


def part_one():

    root = Directory(name = '/')
    state = State(root)

    for line in data:
        pass

def first_marker_position(signal: str, n: int) -> int:
    '''
    Returns the first position of signal
    where the previous n characters were all unique.
    '''
    for index, char in enumerate(signal[n::], start = n):
        prev_n = signal[index-n:index]
        if len(set(prev_n)) == n:
            position = index
            break

    return position

with open('input_files/day6.txt', 'r') as f:
    data = f.read()

part_one_solution = first_marker_position(signal = data, n = 4)
part_two_solution = first_marker_position(signal = data, n = 14)

print(part_two_solution)