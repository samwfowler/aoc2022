outcomes = {
    'Z': {'A': 8, 'B': 9, 'C': 7}, # Z > win
    'X': {'A': 3, 'B': 1, 'C': 2}, # X > lose
    'Y': {'A': 4, 'B': 5, 'C': 6}  # Y > draw
}
score = 0

with open("input.txt") as file:
    for line in file.read().split('\n'):
        score += outcomes[line.split(' ')[1]][line.split(' ')[0]]

print(score)