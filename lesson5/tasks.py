# Создать матрицу любой размерности
# При вводе числа, программа должны выдать все числа из СТОЛБЦА под номером введеного числа

a = int(input("Enter the size of matrix: "))
matrix = [] 
print("Enter the matrix: ")
for i in range(a): 
    matrix.append(list(map(int, input().split())))
print(matrix)

x = int(input("Enter the column number: "))

for a in range(len(matrix)):
    for b in range(len(matrix[x])):
        print(matrix[a][x - 1])
        break

# Создать матрицу любой размерности
# При вводе числа, программа должны выдать все числа из СТРОКИ под номером введеного числа

y = int(input("Enter the line number: "))

for a in range(len(matrix)):
    print(matrix[y - 1][a], end = ' ')