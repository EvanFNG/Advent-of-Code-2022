# Part 1



with open('input_files/day1_1.txt', 'r') as f:
    data = f.read().splitlines()

elf_count = data.count('') + 1

elf_dict = {i + 1: [] for i in range(elf_count)}

current_elf = 1

for i in data:
    if i != '':
        elf_dict[current_elf].append(int(i))
    else:
        current_elf += 1

elf_sum = {k: sum(v) for k, v in elf_dict.items()}

# Answer to part one
print(max(elf_sum.values()))

# Part two: find the total calories of the top three elves

calories_list = [i for i in elf_sum.values()]

calories_list.sort()

top_three = calories_list[-1:-4:-1]

# Answer to part two
print('\n', sum(top_three))