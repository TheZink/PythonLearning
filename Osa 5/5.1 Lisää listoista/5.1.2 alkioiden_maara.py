def laske_alkiot(matrix: list, tofind: int):
    time = 0
    for a in matrix:
        for b in a:
            if b == tofind:
                time += 1
    return time
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))