with open('input_files/day8_sample.txt', 'r') as f:
    text = f.read().splitlines()
    data = [[int(y) for y in list(x)] for x in text]

# Initial count formula
viz_count = 2 * (len(data[0]) + len(data) - 2)

for i in data:
    print(*i)

print('\n')

for row_index, row in enumerate(data):
    # Determine the three arrays of trees to check
    if row_index == 0:
        tree_lists = [row, data[row_index+1], data[row_index+2]]
    elif row_index == len(data):
        tree_lists = [data[-3], data[-2], row]
    else:
        tree_lists = [data[row_index-1], row, data]



print(viz_count)