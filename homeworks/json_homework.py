import json
 
# Создание словаря
data = {
"name": "Dias",
"surname": "Dinmukhammeduly",
"age": 28
}
 
# Запись словаря в .json-файл
with open("data.json", "w") as json_file:
    json.dump(data, json_file)