def solve_first():
    data = open("input.txt", "r").read().splitlines()
    frequency = [0] * len(data[0])
    gamma, epsilon = '', ''
    for line in data:
        for i in range(len(line)):
            if line[i] == '1':
                frequency[i] += 1
            else:
                frequency[i] -= 1
    for j in range(len(frequency)):
        if frequency[j] > 0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma*epsilon)


def solve_second():
    data = open("input.txt", "r").read().splitlines()
    frequency = [0] * len(data[0])
    ox_gen, co2_scrub = '', ''
    for i in range(len(data[0])): #Oxygen greater loop
        for line in data:
            if line[i] == '1':
                frequency[i] += 1
            else:
                frequency[i] -= 1
        if frequency[i] >= 0:
            frequency[i] = '1'
        else:
            frequency[i] = '0'
        data = list(filter( lambda x : x[i] == frequency[i], data))
        #print(data)
        if len(data) == 1:
            ox_gen = data[0]
            print(f"Ox gen {ox_gen}")
            break
    data = open("input.txt", "r").read().splitlines()
    frequency = [0] * len(data[0])
    for i in range(len(data[0])): #CO2 lesser loop
        for line in data:
            if line[i] == '1':
                frequency[i] += 1
            else:
                frequency[i] -= 1
        if frequency[i] >= 0:
            frequency[i] = '1'
        else:
            frequency[i] = '0'
        data = list(filter( lambda x : x[i] != frequency[i], data))
        #print(data)
        if len(data) == 1:
            co2_scrub = data[0]
            print(f"CO2 scrub {co2_scrub}")
            break
    print(f"Multiplied {int(ox_gen, 2) * int(co2_scrub, 2)}")

solve_first()
solve_second()