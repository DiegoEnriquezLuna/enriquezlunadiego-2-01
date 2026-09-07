VACIO = -1

matriz = [
    [1, 2, VACIO, 4],
    [5, VACIO, 7, 8],
    [VACIO, 10, 11, VACIO]
    ]

print("Matriz original")
for fila in matriz:
    for elemento in fila:
        if elemento != VACIO:
            print(elemento, end= " ")
        else:
            print("-1", end=" ")
    print()
    
fila = len(matriz)
columna = len(matriz[0])

for i in range(fila):
    for j in range(columna):
        if matriz[i][j] == VACIO:
            for k in range(i + 1, fila):
                if matriz[k][j] != VACIO:
                    matriz[i][j] = matriz[k][j]
                    matriz[k][j] = VACIO
                    break

print()
print("Matriz recorrida")
for i in range(fila):
    for j in range(columna):
        if matriz[i][j] != VACIO:
            print(matriz[i][j], end=" ")
        else:
            print("-1", end=" ")
    print()
VACIO = -1

matriz = [
    [1, 2, VACIO, 4],
    [5, VACIO, 7, 8],
    [VACIO, 10, 11, VACIO]
    ]

print("Matriz original")
for fila in matriz:
    for elemento in fila:
        if elemento != VACIO:
            print(elemento, end= " ")
        else:
            print("-1", end=" ")
    print()
    
fila = len(matriz)
columna = len(matriz[0])

for i in range(fila):
    for j in range(columna):
        if matriz[i][j] == VACIO:
            for k in range(i + 1, fila):
                if matriz[k][j] != VACIO:
                    matriz[i][j] = matriz[k][j]
                    matriz[k][j] = VACIO
                    break

print()
print("Matriz recorrida")
for i in range(fila):
    for j in range(columna):
        if matriz[i][j] != VACIO:
            print(matriz[i][j], end=" ")
        else:
            print("-1", end=" ")
    print()
