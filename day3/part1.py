def get_priority(char):
    if ord(char) > 96:
        return ord(char) - 96
    else:
        return ord(char) - 38

priority_sum = 0

with open('input.txt') as file:
    rucksack_pairs = file.read().split('\n')
    for rucksack_pair in rucksack_pairs:
        first_rucksack = rucksack_pair[slice(0, int(len(rucksack_pair) / 2))]
        second_rucksack = rucksack_pair[slice(int(len(rucksack_pair) / 2), None)]

        for item in first_rucksack:
            if item in second_rucksack:
                priority_sum += get_priority(item)
        
    print(priority_sum)