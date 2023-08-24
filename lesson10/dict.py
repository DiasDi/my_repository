# Отображения (maps) dict словари 
 
  
 
handbook = { 
    'Swaroop': 'swaroop@swaroopch.com', 
    'Larry': 'larry@wall.org', 
    'Matsumoto': 'matz@ruby-lang.org', 
    'Spammer': 'spammer@hotmail.com', 
} 
 
  
 
dct = { 
    0: '123', 
    1: '456', 
    2: True, 
    3: [True, 3.14, "hello"], 
    4: ('tiger',  
        'elephant',  
        'pinquin', 
    ) 
} 
 
for value in handbook.values(): 
    print(value) 
 
for key in handbook.keys(): 
    print(key) 
 
print(handbook) 
handbook.clear() 
print(handbook) 
 
#fromkeys() - create dictionary 
 
d = dict.fromkeys([1,2,3], "Hello") 
print(d) 
 
#get() - вытащить значение по ключу 
 
print(handbook.get("Matsumoto")) 
 
#copy() - копирование словаря 
 
new_handbook = handbook.copy() 
print(new_handbook) 
print(type(new_handbook)) 
 
#items() - ключи и значения 
 
for key, item in handbook.items(): 
    print(key, "----", item)