def solve_first():
    data = open("input.txt", "r").read().splitlines()
    horizontal_position = 0
    depth = 0
    for line in data:
        if line.startswith("forward"):
            horizontal_position += int(line.split()[1])
        elif line.startswith("up"):
            depth -= int(line.split()[1])
        elif line.startswith("down"):
            depth += int(line.split()[1])
    print(f"horizontal_position: {horizontal_position}")
    print(f"depth: {depth}")
    print(f"multiplied: {horizontal_position*depth}")


def solve_second():
    data = open("input.txt", "r").read().splitlines()
    horizontal_position = 0
    aim = 0
    depth = 0
    for line in data:
        if line.startswith("forward"):
            horizontal_position += int(line.split()[1])
            depth += aim * int(line.split()[1])
        elif line.startswith("up"):
            aim -= int(line.split()[1])
        elif line.startswith("down"):
            aim += int(line.split()[1])
    print(f"horizontal_position: {horizontal_position}")
    print(f"depth: {depth}")
    print(f"multiplied: {horizontal_position*depth}")


solve_first()
solve_second()
