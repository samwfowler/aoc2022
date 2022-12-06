move_id = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
results = {'-1': 'lose', '2': 'lose', '1': 'win', '-2': 'win', '0': 'draw'}
score = 0

for line in open('input.txt').read().split('\n'):
    elf = line.split(' ')[0]
    human = line.split(' ')[1]
    result = results[str(move_id[human] - move_id[elf])]

    score += move_id[human]

    if result == 'win': 
        score += 6
    elif result == 'draw': 
        score += 3

print(score)
