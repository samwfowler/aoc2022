move_id = {'A': 1, 'B': 2, 'C': 3}
outcomes = {
    'Z': {1: 8, 2: 9, 3: 7}, # Z > win
    'X': {1: 3, 2: 1, 3: 2}, # X > lose
    'Y': {1: 4, 2: 5, 3: 6}  # Y > draw
}
score = 0

with open("input.txt") as file:
    for line in file.read().split('\n'):
        elf_move = move_id[line.split(' ')[0]]
        score += outcomes[line.split(' ')[1]][elf_move]

print(score)