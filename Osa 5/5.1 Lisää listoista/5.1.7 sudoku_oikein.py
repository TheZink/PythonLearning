def sudoku_oikein(sudoku: list): #Funktio tarkastaa sudokun rivit läpi, onko siinä toistuvia numeroita 1-9 väliltä
    for row in sudoku:
        for number in row:
            if number > 0:
                if number in check:
                    print("Vaaka toimii", False)
                    return False
                check.append(number)
        check.clear()
    print("Vaaka toimii", True)
    return True

def sudoku_oikein_pysty(sudoku: list): #Funktio tarkastaa sudokun numerot pystysuunnassa läpi
    time1, time2 = 0, 1
    while time2 <= len(sudoku[0]):
        for row in sudoku:
            if row[time1] > 0:
                if row[time1] in check:
                    print("Pysty toimii", False)
                    return False
                check.append(row[time1])
        check.clear()
        time1 += 1
        time2 += 1
    print("Pysty toimii", True)
    return True

def sudoku_oikein_ruudukko(sudoku: list): #Funktio tarkastaa sudoku-ruudukon 3x3 numerot läpi
    row, column = 0, 0
    while row < len(sudoku):
        for r in range(row, row+3):
            for c in range(column, column+3):
                number = sudoku[r][c]
                if number > 0 and number in check:
                    print("Ruudukko toimii", False)
                    return False
                check.append(number)
        check.clear()
        column += 3
        if column == len(sudoku[0]):
            column = 0
            row += 3
        if row == len(sudoku):
            break
    print("Ruudukko toimii", True)
    return True

if __name__ == "__main__":
    check = []
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_oikein(sudoku)
    sudoku_oikein_pysty(sudoku)
    sudoku_oikein_ruudukko(sudoku)

#Alla koodi, mikä meni TMC läpi

# def sudoku_oikein(sudoku: list):
# #Funktio tarkastaa sudokun rivit läpi, onko siinä toistuvia numeroita
#     check = []
#     for row in sudoku:
#         for number in row:
#             if number > 0:
#                 if number in check:
#                     return False
#                 check.append(number)
#         check.clear()
# #Funktio tarkastaa sudokun numerot pystysuunnassa läpi
#     time1, time2 = 0, 1
#     while time2 <= len(sudoku[0]):
#         for row in sudoku:
#             if row[time1] > 0:
#                 if row[time1] in check:
#                     return False
#                 check.append(row[time1])
#         check.clear()
#         time1 += 1
#         time2 += 1
# #Funktio tarkastaa sudoku-ruudukon (3x3) numerot läpi
#     row, column = 0, 0
#     while row < len(sudoku):
#         for r in range(row, row+3):
#             for c in range(column, column+3):
#                 number = sudoku[r][c]
#                 if number > 0 and number in check:
#                     return False
#                 check.append(number)
#         check.clear()
#         column += 3
#         if column == len(sudoku[0]):
#             column = 0
#             row += 3
#         if row == len(sudoku):
#             break
#     return True

# if __name__ == "__main__":
#     sudoku = [
#         [9, 0, 0, 0, 8, 0, 3, 0, 0],
#         [2, 0, 0, 2, 5, 0, 7, 0, 0],
#         [0, 2, 0, 3, 0, 0, 0, 0, 4],
#         [2, 9, 4, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 7, 3, 0, 5, 6, 0],
#         [7, 0, 5, 0, 6, 0, 4, 0, 0],
#         [0, 0, 7, 8, 0, 3, 9, 0, 0],
#         [0, 0, 1, 0, 0, 0, 0, 0, 3],
#         [3, 0, 0, 0, 0, 0, 0, 0, 2]
#     ]
#     sudoku_oikein(sudoku)
        

        