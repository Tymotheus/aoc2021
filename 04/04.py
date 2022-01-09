class BingoBoard():

    def __init__(self, input):
        i, j = 0, 0
        self.board = [[[0 for x in range(2)] for x in range(5)] for x in range(5)]
        for line in input:
            j=0
            numbers = line.split()
            for num in numbers:
                self.board[i][j][0] = int(num)
                j+=1
            i+=1

    def check_if_solved(self):
        """Checks if there is already bingo on this board """
        for i in range(5):
            for j in range(5):
                if self.board[i][j][1] == 0:
                    break
            else: #5 marked in a row
                return True
            for j in range(5):
                if self.board[j][i][1] == 0:
                    break
            else: #5 marked in a column
                return True
        return False

    def mark(self, number):
        for line in self.board:
            for num in line:
                if num[0] == number:
                    num[1] = 1
                    return

    def sum_unmarked(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j][1] == 0:
                    sum += self.board[i][j][0]
        return sum

    def __str__(self):
        return str(self.board[0]) + "\n" + str(self.board[1]) + "\n" + str(self.board[2]) + "\n" + \
        str(self.board[3]) + "\n" + str(self.board[4])


def solve_first():
    data = open("input.txt", "r").read().splitlines()
    data = [line for line in data if line != '']
    bingo_numbers = data.pop(0)
    bingo_numbers = [int(x) for x in bingo_numbers.split(',')]
    print(bingo_numbers)
    boards = list()
    while len(data) > 0:
        board_lines = []
        for i in range(5):
            board_lines.append(data.pop(0))
        boards.append(BingoBoard(board_lines))
    print(f"Number of boards: {len(boards)}")
    for number in bingo_numbers:
        for board in boards:
            board.mark(number)
            if board.check_if_solved() == True:
                print(f"Bingo for number {number}")
                print(f"Solution: {board.sum_unmarked() * number}")
                return


def solve_second():
    data = open("input.txt", "r").read().splitlines()
    data = [line for line in data if line != '']
    bingo_numbers = data.pop(0)
    bingo_numbers = [int(x) for x in bingo_numbers.split(',')]
    print(bingo_numbers)
    boards = list()
    while len(data) > 0:
        board_lines = []
        for i in range(5):
            board_lines.append(data.pop(0))
        boards.append(BingoBoard(board_lines))
    print(f"Number of boards: {len(boards)}")
    for number in bingo_numbers:
        for board in boards.copy():
            board.mark(number)
            if board.check_if_solved() == True:
                if(len(boards)>1):
                    boards.remove(board)
                else:
                    print(board)
                    print(f"Number of boards left: {len(boards)}")
                    print(f"Bingo for number {number}")
                    print(f"Solution: {board.sum_unmarked() * number}")
                    return

solve_first()
solve_second()
