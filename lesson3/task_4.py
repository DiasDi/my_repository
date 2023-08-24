"""
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово "YES", а если в разные цвета — то "NO".
Программа получает на вход ЧЕТЫРЕ ЧИСЛА от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для ПЕРВОЙ клетки, потом для ВТОРОЙ клетки.
"""

a1 = int(input("Enter the first number of the chess figure A: "))
a2 = int(input("Enter the second number of the chess figure A: "))
b1 = int(input("Enter the first number of the chess figure B: "))
b2 = int(input("Enter the second number of the chess figure B: "))

#Опять скобками воспользовался, хотя я знаю, что сперва идет AND, затем OR
#Хотелось сделать условие с тем, что проверяет неправильные значения, но тогда выходить некрасиво
if ((a1 + a2) % 2 == 0 and (b1 + b2) % 2 == 0) or ((a1 + a2) % 2 != 0 and (b1 + b2) % 2 != 0):
	print("YES")
else:
	print("NO")