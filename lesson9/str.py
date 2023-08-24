string = "hello World"

#capitalize() - возвращает текст с заглавной буквы
capitalized_str = string.capitalize()
print(capitalized_str)

#count(substr) - количество вхождений substr в строке
print(string.count("ll"))

#endswith/startswith(suffix) - возвращает True/False если текст заканчивается/начинается на suffix
print(string.endswith("d!!"))
print(string.startswith("hello"))

# index(suffix) - начало индексации в строке
print(string.index("lo"))

#isdigit() - проверка строки на цифру
print("123".isdigit())

#islower/isupper() - возвращает True/False если вся строка с маленькими/большими буквы
print("CAPS LOCK".islower())
print("CAPS LOCK".islower())

#join() - соединяет строки из списка в строку
print(" ".join(["Hello", "World"]))

#split() - разделяет строку
print("Hello world".split())

#strip() - удаляет пробел/знаки препинания
print("    Hello World   -   ".strip())

#upper()/lower() - превращает строку в заглавную/маленькие буквы
print("Hello World".upper())
print("Hello World".lower())