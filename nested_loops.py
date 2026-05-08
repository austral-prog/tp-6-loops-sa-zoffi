def flatten(matrix):
    lst=[]
    for fila in matrix:
        for valor in fila:
            lst.append(valor)
    return lst

def row_sums(matrix):
    lst=[]
    for fila in matrix:
        total=0
        for valor in fila:
            total=total+valor
        lst.append(total)
    return lst

def col_sums(matrix):
    lst=[]
    if len(matrix)>0:
        for col in range(len(matrix[0])):
            total = 0
            for row in range(len(matrix)):
                total += matrix[row][col]
            lst.append(total)
        return lst
