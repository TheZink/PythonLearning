def nelio_oikein(sudoku: list, row: int, col: int):
    check = []
    time = 0
    a = col
    while time < 3:
        time2 = 0
        while time2 < 3:
            if sudoku[row][a] > 0:
                if sudoku[row][a] in check:
                    return False
                check.append(sudoku[row][a])
            a += 1
            time2 += 1
        a = col
        time += 1
        row += 1
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(nelio_oikein(sudoku, 0, 1))
    print(nelio_oikein(sudoku, 1, 2))
