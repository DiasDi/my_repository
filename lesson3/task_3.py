"""
Даны ТРИ целых числа. Определите, сколько среди них СОВПАДАЮЩИХ.
Программа должна вывести ОДНО из чисел:
3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны). 
"""

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

if a == b == c:
	print(3)
elif a == b or a == c or b == c:
	print(2)
else:
	print(0)