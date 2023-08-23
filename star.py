#!/usr/bin/python3


def getArguments():
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./start")
        exit(1)
    return int(sys.argv[1])


if __name__ == "__main__":
    size = int(getArguments())

    if size < 0:
        print("Usage: ./star")
        exit()
    elif size == 0:
        exit()
    else:
        rows = size * 4 + 1
        cols = size * 6 + 1
        board = [[" " for i in range(cols)] for j in range(rows)]

        middle_row = int(rows / 2)
        middle_col = int(cols / 2)

        board[0][middle_col] = "*"

        first_row_pointer = middle_col - 1
        last_row_pointer = middle_col + 1

        row = 1

        for i in range(size - 1):
            board[row][first_row_pointer] = "*"
            board[row][last_row_pointer] = "*"
            first_row_pointer -= 1
            last_row_pointer += 1
            row += 1

        while first_row_pointer != -1:
            board[row][first_row_pointer] = "*"
            board[row][last_row_pointer] = "*"
            first_row_pointer -= 1
            last_row_pointer += 1

        first_row_pointer += 2
        last_row_pointer -= 2
        row += 1

        for i in range(size):
            board[row][first_row_pointer] = "*"
            board[row][last_row_pointer] = "*"
            first_row_pointer += 1
            last_row_pointer -= 1
            row += 1

        for i in range(middle_row):
            board[rows - i - 1] = board[i]

        for row in board:
            while row[-1] == " ":
                row.pop()

        for row in board:
            print("".join(row))
