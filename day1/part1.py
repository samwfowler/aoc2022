max_total = 0
curr_total = 0
for line in open("input.txt").read().split('\n'):
    if line: 
        curr_total += int(line)
    else:
        max_total = max(max_total, curr_total)
        curr_total = 0
print(max_total)