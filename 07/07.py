from statistics import median


def solve_first():
    data = open("input.txt", "r").read().split(',')
    data = list(map(int, data))
    center = median(data)
    print(center)
    summed = 0
    for i in data:
        summed += abs(center-i)
    print(summed)


def solve_second():
    """There's somewhere a bug here, making the result 'slightly wrong'..."""
    data = open("input.txt", "r").read().split(',')
    data = list(map(int, data))
    center = round(sum(data)/len(data))
    print(center)
    summed = 0
    for i in data:
        difference = abs(center-i)
        summed += ((difference+1)*difference)//2
    print(summed)


def alternative_solve_second():
    """Don't like this solution but it works. """
    data = open("input.txt", "r").read().split(',')
    data = list(map(int, data))
    min_value = 191638956
    for center in range(min(data), max(data)):
        summed = 0
        for i in data:
            difference = abs(center - i)
            summed += ((difference+1)*difference)//2
        if summed < min_value:
            min_value = summed
    print(min_value)


solve_first()
solve_second()
alternative_solve_second()