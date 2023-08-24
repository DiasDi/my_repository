"""Даны ТРИ целых числа. Выведите значение НАИМЕНЬШЕГО из них."""

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

if a <= b and a <= c:
	print("Minimum value =", a)
elif b <= a and b <= c:
	print("Minimum value =", b)
else:
	print("Minimum value =", c)