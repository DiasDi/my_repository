# Осуществить ВВОД сторон и расчет площади фигур с выводом по шаблону:
# Площадь <название фигуры> равна <результат>

# 3.14

# S = a * a = a2 (квадрат)
# S = a * b (прямоугольник)
# S = π * r * r = π * r2 (круг)
# S = 1/2 * b * h (прямоугольного треугольника)

pi = 3.14

a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
r = int(input("Введите радиус: "))
h = int(input("Введите высоту: "))

print("Площадь квадрата = ", a * a)
print("Площадь прямоугольника = ", a * b)
print("Площадь круга = ", pi * r**2)
print("Площадь прямоугольного треугольника = ", 1 / 2 * b * h)