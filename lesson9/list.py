# append - add object to the last

lst = [1, 2, 3]
print(lst)
lst.append(4)
print(lst)

#extend() - add objects to the list

new_lst = [5, 6, 7]
lst.extend(new_lst)
print(lst)

#insert() - добавляет объект через индекс

lst.insert(6, "hello")
print(lst)

#remove - delete
lst.remove("hello")
lst.remove(1)
print(lst)

#pop() - удаляет и возвращает через индекс
a = lst.pop()
print(lst)
print(a)

# count() - возвращает количество объекта

count_of_world = lst.count('world')
print(lst)
print(count_of_world)

#clear - очистка

lst.clear()
print(lst)

#copy() - копирование (поверхностное)

new_list = lst.copy()
print(id(lst))
print(id(new_list))

#reverse() - разворачивает список

lst.reverse()
print(lst)

#sort - сортировка

lst.sort()
print(lst)