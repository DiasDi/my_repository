"""
Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите "YES", иначе выведите "NO".
Напоминаю, что в соответствии с григорианским календарем, год является високосным,
если его номер КРАТЕН 4, но НЕ КРАТЕН 100, а также если он КРАТЕН 400. 
"""
year = int(input("Enter the year: "))
# Можно было и не ставить скобки, но мне так спокойнее
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print("YES")
else:
	print("NO")