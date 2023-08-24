# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

if a < b:
    for x in range(a, b + 1):
        print(x, end=" ")
else:
    for x in range(a, b - 1, -1):
        print(x, end=" ")