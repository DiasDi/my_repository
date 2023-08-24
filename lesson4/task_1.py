# Даны два целых числа A и B (при этом A <= B). Выведите все числа от A до B включительно.

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

print(list(range(a,b+1)))

for i in range(a, b + 1):
    print(i, end = " ")