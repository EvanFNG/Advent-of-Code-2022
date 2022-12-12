class Point:
    def __init__(self, coords: list[int]) -> None:
        self.coords = coords

    def __repr__(self) -> str:
        return f'{self.coords}'

    def neighbors(self) -> list[list[int]]:
        x,y = self.coords
        return [ [x+1, y], [x-1, y], [x, y-1], [x, y+1], [x-1, y+1], [x-1, y-1], [x+1, y-1], [x+1, y+1] ]

    def is_neighbor(self, pt: 'Point') -> bool:
        return (self.coords in pt.neighbors()) or (self.coords == pt.coords)

    def update_location(self, dx: int, dy: int) -> None:
        self.coords[0] += dx
        self.coords[1] += dy

    def coords(self):
        return self.coords

def process_move(s: str) -> list:
    '''
    Reads moves from the input file
    and returns the corresponding list

    >>> process_move('D 4')
    [0, -4] 
    '''
    commands = s.split()
    direction = commands[0]
    amount = int(commands[1])

    match direction:
        case 'R':
            return [amount, 0]

        case 'L':
            return [-amount, 0]

        case 'U':
            return [0, amount]

        case 'D':
            return [0, -amount]

def difference(l1: list, l2: list) -> list:
    '''
    Returns the arithmetic difference
    of elements between l1 and l2.

    >>> difference([4, 5], [3, 4])
    [1, 1]
    '''
    return [x - y for x, y in zip(l1, l2)]


head = Point([0, 0])
tail = Point([0, 0])

print(difference(head.coords, tail.coords))
