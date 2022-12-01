# Sample Solution Part 1:

with open('input_files/day1_1_sample.txt', 'r') as f:
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

print(elf_sum)
print(max(elf_sum, key = elf_sum.get))