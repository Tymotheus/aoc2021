def solve_first():
    data = open("input.txt", "r").read().split(',')
    data = list(map(int, data))

    for day in range(256):
        fish = data.copy()
        for i in range(len(fish)):
            if data[i] == 0:
                data.append(8)
                data[i] = 6
            else:
                data[i] -= 1
    print(len(data))

solve_first()