def rotate(self, matrix):
    for x in range(len(matrix)):
        matrix.insert(x, matrix.pop())

    for y in range(len(matrix)):
        for z in range(y + 1, len(matrix)):
            temp = matrix[y][z]
            matrix[y][z] = matrix[z][y]
            matrix[z][y] = temp
