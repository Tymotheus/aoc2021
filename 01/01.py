def solve_first():
    data = open("input.txt", "r").read().splitlines()
    tab = [int(i) for i in data]
    increments = 0
    for a, b in zip(tab, tab[1:]):
        if a < b:
            increments += 1
    return increments


def solve_second():
    data = open("input.txt", "r").read().splitlines()
    tab = [int(i) for i in data]
    increments = 0
    previous_three_sum = sum(tab[:2])
    new_three_sum = 0
    for i in range(3, len(tab)):
        new_three_sum = previous_three_sum + tab[i] - tab[i-3]
        if new_three_sum > previous_three_sum:
            increments += 1
        new_three_sum = previous_three_sum
    return increments


print(solve_first())
print(solve_second())
