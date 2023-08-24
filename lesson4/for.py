# Факториалом числа n называется произведение 1 * 2 * ... * n. Обозначение: n!.
# По данному натуральному n вычислите значение n!

# Например, 3! => на выходе получаем 6
a = int(input("Enter the number for factorial operation: "))

sum = 1
for x in range(1, a+1):
    sum *= x
print(f"Factorial of number {a} is {sum}")