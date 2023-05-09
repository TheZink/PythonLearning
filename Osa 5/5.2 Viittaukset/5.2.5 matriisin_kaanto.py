def transponoi(matrix: list):
    new_matrix = zip(*matrix)
    matrix.clear()
    time = 0
    for a in new_matrix:
        matrix.append([])
        for b in a:
            matrix[time].append(b)
        time += 1

if __name__ == "__main__":
    matrix = [[1,2],[1,2]]
    transponoi(matrix)
    print(matrix)

# def transponoi(matriisi: list):
#     n = len(matriisi)
#     for i in range(n):
#         for j in range(i, n):
#             temp = matriisi[i][j]
#             matriisi[i][j] = matriisi[j][i]
#             matriisi[j][i] = temp