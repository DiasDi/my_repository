# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.

sum = 0

for x in range(10):
    a = int(input(f'Enter the number #{x+1}: '))
    sum+=a
print("Sum: ", sum)
