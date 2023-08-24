v1 = int(input("Enter the volume #1: "))
v2 = int(input("Enter the volume #2: "))
t1 = int(input("Enter the temperature #1: "))
t2 = int(input("Enter the temperature #2: "))

v = v1 + v2
t = (v1 * t1 + v2 + t2) / (v1+v2)

print("Volume =", v)
print("Temperature =", t)