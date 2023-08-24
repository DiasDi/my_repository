"""
Дан двумерный массив `matrix`.
Поменяйте в массиве столбцы с номерами i и j и выведите результат.
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

x = int(input("Enter the number x (1-3): "))
y = int(input("Enter the number y (1-3): "))

# 1 2 3       1 3 2
# 4 5 6   =>  4 6 5
# 7 8 9       7 9 8

# Вывод первоначальной матрицы

for a in range(len(matrix)):
    for b in range(len(matrix)):
        print(matrix[a][b], end=" ")
    print()

print()

for a in range(len(matrix)):
    for b in range(len(matrix[a])):
        if b == x:
            matrix[a][x-1], matrix[a][y-1] = matrix[a][y-1], matrix[a][x-1]
            break
        if b == y:
            matrix[a][y-1], matrix[a][x-1] = matrix[a][x-1], matrix[a][y-1]
        
for a in range(len(matrix)):
    for b in range(len(matrix)):
        print(matrix[a][b], end=" ")
    print()