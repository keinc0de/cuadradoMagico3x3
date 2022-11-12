def fila(num_fila, lista):
    res = 0
    for col in range(len(lista)):
        res += lista[num_fila][col]
    return res

def Columna(num_col, lista):
    res = 0
    for col in range(len(lista)):
        res += lista[col][num_col]
    return res

def diagonalNoSe(lista):
    res = 0
    for x in range(len(lista)):
        res += lista[x][x]
    return res

def diagonalNeSo(lista):
    res = 0
    n = len(lista)
    for x in range(n):
        res += lista[x][(n-1)-x]
    return res