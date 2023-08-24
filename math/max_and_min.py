a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
if a >= b and a >= c:
    print("Maximum value is ",a)
elif b >= a and b >= c:
    print("Maximum value is ",b)
elif c >= a and c >= b:
    print("Maximum value is ",c)
else:
    print("Same value is ",a)