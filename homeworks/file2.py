import random

file_name = "file2_abramyan.txt"
number = int(input("Enter the number: "))
try:
    f = open(file_name, "w")
    f.write(f'Entered number is {number}' '\n')
    try:
        for i in range(number):
            f.write((str)((i+1)*2) + '\n')
    finally:
        f.close()
except:
    print('Файл не создан')