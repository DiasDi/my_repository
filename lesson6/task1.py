# Реализовать собственную функцию `len`, который называется `len_self`

# Пример как работает встроенная фун-ия len:
print(len([1, 2, 3]))

def len_self(message):
    sum = 0
    for i in message:
        sum += 1
    print(sum)

len_self("Dias")
