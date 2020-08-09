from functools import reduce


def warshall(a):
    # Checks  the matrix is square

    assert (len(row) == len(a) for row in a)

    # Number of elements in the matrix
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # we use the ord with the original positions  i, j  because  we want  to mantain the connections in the matrix
                # We search here if there is  any pair i,k that has transitvity to k,j
                # So  if this happens i,j would have a new connection though i,k and k,j
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a


def teoremFour(mr: list) -> list:
    # Checks  the matrix is square
    assert (len(row) == len(mr) for row in mr)
    n = len(mr)
    currentMatrix = mr.copy()
    matrices = []
    for i in range(n - 1):
        holder = [[None for _ in range(n)] for _ in range(n)]
        for index, row in enumerate(currentMatrix):

            for indexColumn, column in enumerate(row):
                productRow = 0
                for k in range(n):
                    productRow += currentMatrix[k][indexColumn] * currentMatrix[index][k]
                try:
                    holder[index][indexColumn] = productRow and 1
                    mr[index][indexColumn] = mr[index][indexColumn] or holder[index][indexColumn]
                except:
                    print("lol")
        matrices.append(holder)
        currentMatrix = holder.copy()
    #
    # for matrix in matrices:
    #     for indexRow, row in enumerate(matrix):
    #         for indexColumn, column in enumerate(row):
    #             mr[indexRow][indexColumn] = mr[indexRow][indexColumn] or column

    return mr

print("---WARSHALL ALGORITHM---")
print(warshall([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]))

print("---Teorema 4---")
print(teoremFour([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]))
