n = int(input("Enter the count of numbers: "))

summ_zero = 0

for i in range(n):
    a = int(input(f"Enter the number #{i+1}:"))
    if a == 0:
        summ_zero += 1
print(f"I am counted {summ_zero} zero(-s)")    