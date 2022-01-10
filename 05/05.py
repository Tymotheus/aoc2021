from math import copysign

def solve_first():
    data = open("input.txt", "r").read().splitlines()
    board = [[0 for i in range(1000)] for j in range(1000)]
    for line in data:
        line = line.split(' -> ')
        starting_position = tuple(map(int, line[0].split(',')))
        ending_position = tuple(map(int, line[1].split(',')))
        # case that line is diagonal
        if starting_position[0] != ending_position[0] and \
                starting_position[1] != ending_position[1]:
            continue
        if starting_position[0] != ending_position[0]:        # horizontal line
            for i in range(min(starting_position[0], ending_position[0]),
                           max(starting_position[0], ending_position[0]) + 1):
                board[i][starting_position[1]] += 1
        else:   # vertical line
            for j in range(min(starting_position[1], ending_position[1]),
                           max(starting_position[1], ending_position[1]) + 1):
                board[starting_position[0]][j] += 1
    overlaps = 0
    for line in board:
        for element in line:
            if element > 1:
                overlaps += 1
    print(overlaps)

def solve_second():
    data = open("input.txt", "r").read().splitlines()
    board = [[0 for i in range(1000)] for j in range(1000)]
    for line in data:
        line = line.split(' -> ')
        starting_position = tuple(map(int, line[0].split(',')))
        ending_position = tuple(map(int, line[1].split(',')))
        # case that line is diagonal
        if starting_position[0] != ending_position[0] and \
                starting_position[1] != ending_position[1]:
            for i in range(abs(ending_position[0] - starting_position[0]) + 1):
                board[starting_position[0] + int(copysign(i, ending_position[0]-starting_position[0]))][starting_position[1] + int(copysign(i, ending_position[1]-starting_position[1]))] += 1
        else: #vertical or horizontal
            if starting_position[0] != ending_position[0]:        # horizontal line
                for i in range(min(starting_position[0], ending_position[0]),
                               max(starting_position[0], ending_position[0]) + 1):
                    board[i][starting_position[1]] += 1
            else:   # vertical line
                for j in range(min(starting_position[1], ending_position[1]),
                               max(starting_position[1], ending_position[1]) + 1):
                    board[starting_position[0]][j] += 1
    overlaps = 0
    for line in board:
        for element in line:
            if element > 1:
                overlaps += 1
    print(overlaps)

solve_first()
solve_second()