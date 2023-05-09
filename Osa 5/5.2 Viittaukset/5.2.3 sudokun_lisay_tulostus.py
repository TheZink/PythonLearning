import copy
def tulosta(a):
    column, row = 0, 0
    while row < len(sudoku):
        for b in range(row, row+3):
            number2 = a[b]
            while column < len(number2):
                for c in range(column, column+3):
                    number = number2[c]
                    if number == 0:
                        print("_ ", end="")
                    else:
                        print(f"{number} ", end="")
                    #print(end="")
                print(" ", end="")
                column += 3
            print("")
            column = 0
        print()
        row += 3
    return sudoku

def kopioi_ja_lisaa(sudoku: list, row: int, col: int, number: int) -> list:
    kopio = []
    for a in sudoku:
        kopio.append(a[:])
    kopio[row][col] = number
    return kopio

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)