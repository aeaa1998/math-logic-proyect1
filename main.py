import numpy as np

def warshall(a):
    # Checks  the matrix is square

    assert (len(row) == len(a) for row in a)

    # Numero de elementos en la matriz
    n = len(a)
    for m in range(n):
        for i in range(n):
            for j in range(n):
                # usamos a[i][j] or (a[i][m] and a[m][j]) porque queremos guardar la connecion ya obtenida de la matriz original
                # Miramos is hay un par ik, que  tenga  transitividad  con k,j para saber que hay vertices interiores dentro de  i,j
                # E ir llenando la matriz de cierre transitivo.
                a[i][j] = a[i][j] or (a[i][m] and a[m][j])
    return a


def teoremFour(mr: list) -> list:
    # Checks  the matrix is square
    assert (len(row) == len(mr) for row in mr)
    n = len(mr)
    currentMatrix = mr.copy()
    matrices = []

    # Se itera el numero de n - 1 veces para tener las matrices Rn se itera n-1 debido a que 1 es la matriz original
    # Ya se tiene que en este caso es mr
    for i in range(n - 1):
        holder = [[None for _ in range(n)] for _ in range(n)]
        for index, row in enumerate(currentMatrix):
            for indexColumn, column in enumerate(row):
                productRow = 0
                for k in range(n):
                    # Hace profucto punto para saber el valor de la matriz Rn en el punto index, indexColumn
                    productRow += currentMatrix[k][indexColumn] * currentMatrix[index][k]

                # Guarda la matriz para realizar la siguiente matriz al cuadrado
                # Se usa and para  guardar 1 o 0
                holder[index][indexColumn] = productRow and 1
                # Or con el valor del resultado de Rn para ir viendo los puntos que conecta indirectamente
                mr[index][indexColumn] = mr[index][indexColumn] or holder[index][indexColumn]

        matrices.append(holder)
        currentMatrix = holder.copy()

    return mr

print("---WARSHALL ALGORITHM---")
print(np.matrix(warshall([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])))

print("---Teorema 4---")
print(np.matrix(teoremFour([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])))
