#

n = int(input("Enter the number: "))
lst = []

for i in range(n):
    a = int(input(f'Enter the element {i+1}: '))
    if a % 2 == 0:
        lst.append(a)
print(lst)

#Ввод элемента в переменную name. Удалить 

element = input("Enter the element: ")
lst = ["user1", True, 321, 3.14, "user1", "", 123]
lst.append(element)

new_lst = list(set(lst))

print(new_lst)

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)
print(new_list)