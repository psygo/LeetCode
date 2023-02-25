def spiralOrder(matrix):
    spiral = []
    rowSize = len(matrix)
    colSize = len(matrix[0])
    total = rowSize * colSize

    initRow, endRow = 0, rowSize
    initCol, endCol = 0, colSize

    while len(spiral) < total:
        # Top
        for i in range(initCol, endCol):
            # print(matrix[initRow][i])
            spiral.append(matrix[initRow][i])

        if len(spiral) == total:
            break

        # Right
        for i in range(initRow + 1, endRow):
            spiral.append(matrix[i][endCol - 1])

        if len(spiral) == total:
            break

        # Bottom
        for i in range(endCol - 1, initCol, -1):
            spiral.append(matrix[endRow - 1][i - 1])

        if len(spiral) == total:
            break

        # Left
        for i in range(endRow - 1, initRow + 1, -1):
            spiral.append(matrix[i - 1][initCol])

        initRow += 1
        endRow -= 1
        initCol += 1
        endCol -= 1

    return spiral


# print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
