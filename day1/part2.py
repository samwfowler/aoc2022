totals = []
curr_total = 0
for line in open("input.txt").read().split('\n'):
    if line:
        curr_total += int(line)
    else:
        totals.append(curr_total)
        curr_total = 0
totals.sort()
totals.reverse()
print(sum(totals[0:3]))