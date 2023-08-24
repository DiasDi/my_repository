limit = int(input("Enter the number: "))

for x in range(limit+1):
    if x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')