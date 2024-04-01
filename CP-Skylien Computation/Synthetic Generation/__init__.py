import random

num_lines =10000 # Number of lines to select

with open('data.txt', 'r') as f:
    lines = f.readlines()

selected_lines = random.sample(lines, num_lines)

with open('10k_data.txt', 'w') as f:
    f.writelines(selected_lines)

