samples = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',
]


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