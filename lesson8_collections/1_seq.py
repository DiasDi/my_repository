#List (can change)
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(shoplist[0], shoplist[1], shoplist[2], shoplist[3])
del shoplist[0]
print('apple' in shoplist)
print('orange' in shoplist)
print(len(shoplist))

for item in shoplist:
    print(item)

#Tuples (can not change)

zoo = ('python', 'elephant', 'penguin') # zoo = 'python', 'elephant', 'penguin'
zoo_2 = ('тигр',)

print(zoo)
print(zoo[0])
print(len(zoo))

for animal in zoo:
    print(animal, end = " ")

new_zoo = 'monkey', 'giraffe', zoo
new_zoo = zoo + zoo_2
print(new_zoo[-1])
print(new_zoo[2][1])

#String

string = "My name is Dias"

print('Dias' in string)
print(string[0])
print(string[-1])

for letter in string:
    print(letter, end = '')