# Даны два целых числа A и В (A > B). 
# Выведите все нечётные числа от A до B включительно,в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

for x in range (a - (a + 1) % 2, b - b % 2, -2):
    print(x, end = " ")